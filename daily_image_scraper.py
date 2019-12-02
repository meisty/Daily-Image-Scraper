import requests, bs4, os

def getDailyImage(imageUrl):
    url=imageUrl
    res = requests.get(imageUrl)
    res.raise_for_status

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    imageElem = soup.select('html body center p a img')
    if imageElem == []:
        print("Could not find the image")
        return False
    else:
        imgUrl = imageElem[0].get('src')
        imgUrl = url+imgUrl
        #download the image
        print("Downloading the image %s..." % (imgUrl))
        res = requests.get(imgUrl)
        res.raise_for_status
        print(res)

    with open('background.jpg', 'wb') as fo:
        for chunk in res.iter_content(4096):
            fo.write(chunk)


    os.system("/usr/bin/gsettings set org.gnome.desktop.background picture-uri file:/home/shaun/python/webscraping/daily_image_scraper/background.jpg")






result = getDailyImage('https://apod.nasa.gov/apod/')
if result == False:
    print("Image failed to download")
else:
    print("Your image has been downloaded and has been set as your desktop background")
