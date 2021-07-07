#! python3
# linkVerification.py - gets every linked page and reports which ones failed to download due to 404 error
#                       args[url]

import requests, os, sys, bs4
from requests.sessions import InvalidSchema


if len(sys.argv) > 1:

    url = sys.argv[1]
    destFolder = os.path.join("C:\Lucas\DownloadedLinks")
    os.makedirs(destFolder, exist_ok=True)

    res = requests.get(url)
    
    res.raise_for_status()

    basePage = bs4.BeautifulSoup(res.text, 'html.parser')

    linkElems = basePage.select('a')

    linkNumber = 0
    for link in linkElems:
        linkNumber += 1
        newUrl = link.get('href')
        try:
            newRes = requests.get(newUrl)
        except Exception:
            print(f'This is not a valid URL {newUrl}')
            continue

        if newRes.status_code != 404:
            thePage = open(os.path.join(destFolder, f'link{linkNumber}.html'), 'wb')
            
            for chunk in newRes.iter_content(100000):
                thePage.write(chunk)

            thePage.close()
        else:
            print(f'{newUrl} has thrown a 404 error')

        