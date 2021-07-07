#! python3

import bs4, requests, os

url = 'https://xkcd.com'
os.makedirs('C:\Lucas\Comics', exist_ok=True)

while not url.endswith('#'):
    
    res = requests.get(url)
    res.raise_for_status()

    pageFile = bs4.BeautifulSoup(res.text, 'html.parser')

    comicElem = pageFile.select('#comic img')
    if comicElem == []:
        print('Could not find comic image.')
    else:
        comicUrl = 'https:' + comicElem[0].get('src')
        # Download the image.
        print('Downloading image... ' + url)
        res = requests.get(comicUrl)
        res.raise_for_status()

        imageFile = open(os.path.join('C:\Lucas\Comics', os.path.basename(comicUrl)), 'wb')

        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()

    #Get the Prev button's url.
    prevLink = pageFile.select('a[rel="prev"]')[0]
    url = 'https://xkcd.com' + prevLink.get('href')

print('Done')
