#! python3
# downloadBasicWebsite.py - downloads the pages of the site https://www.basicwebsiteexample.com/

import os, requests, bs4

baseUrl =  'https://www.basicwebsiteexample.com'

os.makedirs('C:\Lucas\BasicWebsite', exist_ok=True)

linksSelector = '.js-menu-list a'
links = bs4.BeautifulSoup(requests.get(baseUrl).text, 'html.parser').select(linksSelector)

for link in links:
    urlToDownload = baseUrl + link.get('href')
    thePage = open(os.path.join('C:\Lucas\BasicWebsite', link.text.strip()) + '.html', 'wb')

    res = requests.get(urlToDownload)
    
    for chunk in res.iter_content(100000):
        thePage.write(chunk)
    thePage.close()
