import requests
from bs4 import BeautifulSoup
import os

base_url = 'https://rhythm-lab.com/breakbeats'
out_dir = 'breakbeats/'

def scrape_links():
    r = requests.get(base_url)
    soup = BeautifulSoup(r.content, 'html.parser')
    for l in soup.find_all('div', {'class': 'blog_files_item'}):
        a = l.find('a')
        url = a.attrs.get('href')
        if url.endswith('.wav'):
            yield url

def download_url(url):
    fp = os.path.join(out_dir, url.split('/')[-1])
    if os.path.exists(fp):
        print('skipping %s' % fp)
        return
    print('downloading %s' % fp)
    r = requests.get(url)
    with open(fp, 'wb') as f:
        f.write(r.content)

def main():
    try:
        os.mkdir(out_dir)
    except:
        pass
    for l in scrape_links():
        download_url(l)

if __name__ == "__main__":
    main()




