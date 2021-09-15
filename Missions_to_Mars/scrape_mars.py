#!/usr/bin/env python
# coding: utf-8

# Instructional comments noted with single #
## My comments noted with ##

## defining my scrape function as what we did in jupyter notebook

## For this, I get rid of most or all of the print statements that were used in development
def scrape():
    ## Importing my dependencies
    import pandas as pd
    from bs4 import BeautifulSoup as bs
    import requests
    from splinter import Browser
    from webdriver_manager.chrome import ChromeDriverManager
    import time

    ## Pandas isn't used until part 3 but I don't like having dependency imports later\
    ## so I'm importing now
    import pandas as pd

    # Set the URL to be scraped
    url = 'https://redplanetscience.com/'

    # set up splinter

    ## I prefer camelCase variable names but I believe this name has to be with the _
    executable_path = {'executable_path' : ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless = False)

    # Visit the site
    browser.visit(url)

    # Use the browser to get our html
    siteHTML = browser.html

    # Create my beautiful soup
    soup = bs(siteHTML, 'html.parser')


    ## The article titles appear to be hidden in a list_text inside a div.
    ## Let's grab them all
    soupResponse = soup.find_all('div', class_='list_text')


    # ## NASA MARS NEWS

    # Scrape https://redplanetscience.com/ to collect the latest news title and paragraph text
    # Assign the text to variables to be used later

    ## Now that the connection is made, let's start scraping

    ## Big change to my code here from the jupyter notebook. In the notebook I loop through and get all the articles, now I just want to return the first.
    news_title = soup.find('div', class_='content_title').text
    news_p = soup.find('div', class_="article_teaser_body").text    


    # ## JPL Mars Space Images - Featured Image


    ## I believe we can use a similar methodology to the last one

    # First we grab the url
    imagesUrl = 'https://spaceimages-mars.com/'



    ## Set up the browser again
    executable_path = {'executable_path' : ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless = False)

    ## Visit the site
    browser.visit(imagesUrl)


    ## I believe this lets us find the image url
    browser.links.find_by_partial_text('FULL IMAGE').click()


    # Use the browser to get our html
    singleImageHTML = browser.html

    # Create my beautiful soup
    soup = bs(singleImageHTML, 'html.parser')

    ## Took me too long to figure out the 'src' at the end here
    soupResponse = soup.find('img', class_='fancybox-image')['src']


    ## Print out the URL for the featured image!

    featured_image_url = url + soupResponse


    # ## Mars Facts

    ## First things first, we set the url
    factsURL = 'https://galaxyfacts-mars.com'


    ## use read_html to create a dataframe
    scrapedTables = pd.read_html(factsURL)

    ## Let's set that equal to a variable to be used later
    marsFacts = scrapedTables[1]


    ## Then convert that to an html with the to_html methodology
    marsFactsHTML = marsFacts.to_html()


    # ## Mars Hemispheres


    ## As we do every time, set the URL
    hemispheresURL = 'https://marshemispheres.com/'


    ## Use splinter to open the browser
    executable_path = {'executable_path' : ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless = False)

    browser.visit(hemispheresURL)


    # set the html for soup
    hemispheresHTML = browser.html

    # Create my beautiful soup
    soup = bs(hemispheresHTML, 'html.parser')

    ## Do the scrape for the hemisphere names
    hemispheres = soup.find_all('div', class_='item')
    ## I'll have to use hemispheres.h3.text to get the hemisphere names.


    ## Here's where it gets funky
    ## I'm going to use the browser.links.find_by_partial_text().click() 
    ## methodology from above to click the links in splinter
    ## Then I'm going to scrape the info from there


    ## testing web scrape to know where info is
    browser = Browser('chrome', **executable_path, headless = False)
    browser.visit('https://marshemispheres.com/cerberus.html')

    hemiHTML = browser.html
    soup = bs(hemiHTML, 'html.parser')

    hemiSoup = soup.find_all('div', class_='downloads')
    ## Here is where we're going to find the info
    print(hemiSoup[0].li.a['href'])

    ## setting the list to empty for the loop
    hemisphere_image_urls = []

    ## Open a browser
    browser = Browser('chrome', **executable_path, headless = False)

    ## For each hemisphere
    for hemi in hemispheres:
        ## go to the hemisphere
        browser.visit(hemispheresURL)
        hemisphereName = hemi.h3.text
        browser.links.find_by_partial_text(hemisphereName).click()
        hemiHTML = browser.html
        soup = bs(hemiHTML, 'html.parser')
        hemiSoup = soup.find_all('div', class_='downloads')
        hemiImageURL = hemispheresURL + hemiSoup[0].li.a['href']
        hemiDict = {"title" : hemisphereName, "img_url" : hemiImageURL}
        hemisphere_image_urls.append(hemiDict)
        ## let the code chill for a second before running agian
        time.sleep(1)

    marsReturnDict = {}
    marsReturnDict['News Title'] = news_title
    marsReturnDict['News Text'] = news_p
    marsReturnDict['Mars Facts'] = marsFactsHTML
    marsReturnDict['Mars Hemispheres'] = hemisphere_image_urls
    
    return marsReturnDict