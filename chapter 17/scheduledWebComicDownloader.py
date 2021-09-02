#! python3
# scheduledWebComicDownloader.py - Checks a comic website and downloads the new comic if there's any since the las visit.

import os, datetime, requests, bs4, threading


KOS_XPATH = 'div.col-sm-12 > div.blog-story-wrapper'
XKCD_CSS = 'comic-display-name > .comic-date-r'

URLS = {'kos':'https://www.dailykos.com/blog/Comics/', 'fbfw':'http://comics.azcentral.com/slideshow?comic=fb&feature_id=fb'}

todayDate = datetime.datetime.now()
fileDateFormat = r'%Y-%m-%d'
dateForFile = todayDate.strftime(fileDateFormat)

def downloadDailyComicKos():
    res = requests.get(URLS.get('kos'))
    res.raise_for_status()

    print('going for kos')
    comicHtml = bs4.BeautifulSoup(res.text, 'html.parser')
    comicTimeFormat = r'%A %B %d, %Y'
    postDate = comicHtml.select(KOS_XPATH + " div.author-date.hidden-sm > span[data-time-format='" + comicTimeFormat + "']")[0]
    postDate = postDate.get_text()
    print(f'the recent post has date {postDate}')
    if postDate.strip() == todayDate.strftime(comicTimeFormat):
        imgUrl = comicHtml.select(KOS_XPATH + ' div.top-story-image img')[0]
        print(imgUrl.get('src'))
        comicImage = requests.get(imgUrl.get('data-src'))
        saveComic(comicImage, 'kos')


def downloadDailyComicsFbfw():
    res = requests.get(URLS.get('fbfw'))
    res.raise_for_status()

    print('going for fbfw')
    comicHtml = bs4.BeautifulSoup(res.text, 'html.parser')
    comicTimeFormat = r'%B %d, %Y'
    postDate = comicHtml.select('.comic-display-name > .comic-date-r')[0]
    postDate = postDate.getText()
    print(f'the recent post has date {postDate}')
    if postDate.strip() == todayDate.strftime(comicTimeFormat):
        imgUrl = comicHtml.select('.comics-wrapper > img')[0].get('src')
        print(imgUrl)
        comicImage = requests.get(imgUrl)
        saveComic(comicImage, 'fbfw')

def saveComic(image, comicPage):
    imageFile = open(os.path.join('/scratch/home/lastolfi/Education/automatetheboring-python/chapter 17/', comicPage + dateForFile + '.jpg'), 'wb')
    for chunk in image.iter_content(100000):
        imageFile.write(chunk)
    imageFile.close()
        

comicsThreads = []
kosThread = threading.Thread(target=downloadDailyComicKos)
comicsThreads.append(kosThread)
kosThread.start()
fbfwThread = threading.Thread(target=downloadDailyComicsFbfw)
comicsThreads.append(fbfwThread)
fbfwThread.start()


