from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd
import time

def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver 
    executable_path = {'executable_path': 'chromedriver'}
    return Browser('chrome', **executable_path, headless=False)

def scrape():
    browser = init_browser()

    #### URL of page to be scraped - MARS NEWS ####
    url = "https://redplanetscience.com/"
    browser.visit(url)
    html = browser.html
    time.sleep(1)
    # Create BeautifulSoup object and parse
    soup = BeautifulSoup(html, 'html.parser')
    
    # Collect the latest News Title and Paragraph Text and assign text to variables
    news_title = soup.find('div', class_='content_title').text
    news_p = soup.find('div', class_='article_teaser_body').text

    #### URL of page to be scraped - JPL IMAGES ####
    url = "https://spaceimages-mars.com/"
    browser.visit(url)
    html = browser.html
    time.sleep(1)
    # Create BeautifulSoup object and parse
    soup = BeautifulSoup(html, 'html.parser')

    # Find image url for the current Featured Mars Image; assign the url string to a variable
    full_img = soup.find('img', class_='headerimage fade-in')['src']
    featured_image_url = url + full_img

    #### URL of page with tables to be read - MARS FACTS ####
    url = "https://galaxyfacts-mars.com/"
    # Scrape any tabular data from page
    tables = pd.read_html(url)
    
    # Convert the data to a HTML table string
    mars_df = pd.DataFrame(tables[1])
    mars_df.columns = ['Profile Item', 'Fact']
    mars_df.set_index('Profile Item', inplace=True)
    # Generate html table
    mars_table = mars_df.to_html()
    # Clean up table - strip newlines
    mars_table.replace('\n','')

    #### URL of page to be scraped - MARS HEMISPHERES ####
    url = "https://marshemispheres.com/"
    browser.visit(url)
    html = browser.html
    time.sleep(1)
    # Create BeautifulSoup object and parse
    soup = BeautifulSoup(html, 'html.parser')

    # Obtain high resolution images for each of Mar's hemispheres
    products = soup.find_all('div', class_='item')
    hemisphere_image_urls = []
    for product in products:
        hemi_dict = {}
        # Use Beautiful Soup's find() method to navigate and retrieve attributes
        title = product.find('h3').text
        link = product.find('a')['href']
        
        hemi_dict['title'] = title
        hemi_url = 'https://marshemispheres.com/' + link
        
        try:
            browser.visit(hemi_url)
            html = browser.html
            soup = BeautifulSoup(html, 'html.parser')
            
            images = soup.find_all('div', class_='description')
        
            for image in images:
                full_image = image.find('a')['href']
                hemi_dict['img_url'] = 'https://marshemispheres.com/' + full_image
                hemisphere_image_urls.append(hemi_dict)
        except:
            print("Scraping Complete")
    
    # Store data in a dictionary
    mars_data = {
        "news_title": news_title,
        "news_p": news_p,
        "featured_image_url": featured_image_url,
        "mars_table": mars_table,
        "hemisphere_image_urls": hemisphere_image_urls
    }

    browser.quit()

    # Return results
    return mars_data
    

