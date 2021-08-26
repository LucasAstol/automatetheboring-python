#! python3

import bs4, requests, os, threading

url = 'https://xkcd.com'
os.makedirs('C:\Lucas\ComicsThreaded', exist_ok=True)

def downloadXkcd(startComic, endComic):
    for urlNumber in range(startComic, endComic):
        # Download the page.
        print('Downloading page https://xkcd.com/%s...' % (urlNumber))
        res = requests.get('https://xkcd.com/%s' % (urlNumber))
        res.raise_for_status()

        pageFile = bs4.BeautifulSoup(res.text, 'html.parser')

        comicElem = pageFile.select('#comic img')

        if comicElem == []:
            print('Could not find comic image.')
        else:
            comicUrl = 'https:' + comicElem[0].get('src')
            # Download the image.
            print('Downloading image... ' + comicUrl)
            res = requests.get(comicUrl)
            res.raise_for_status()

            imageFile = open(os.path.join('C:\Lucas\ComicsThreaded', os.path.basename(comicUrl)), 'wb')

            for chunk in res.iter_content(100000):
                imageFile.write(chunk)
            imageFile.close()

# Create and start the thread objects.
downloadThreads = []            #a list of all the Thread objects
for i in range(0, 140, 10):     # loops 14 times, creates 14 threads
    start = i
    end = i + 9
    if start == 0:
        start = 1       #There is no comic 0, so set it to 1.
    downloadThread = threading.Thread(target=downloadXkcd, args=(start, end))
    downloadThreads.append(downloadThread)
    downloadThread.start()    

#Wait for all threads to end.    
for downloadThread in downloadThreads:
    downloadThread.join()

print('Done.')