# Web-Scraping-Challenge

## Mission to Mars
***

This assignment builds a web application that scrapes various websites for data related to the Mission to Mars and displays the information in a single HTML page.

### Scraping
* mission_to_mars.ipynb - scraping and analysis of NASA Mars News (title and short paragraph), JPL Mars Space Images (featured image), Mars Facts (table), Mars Hemishpere (titles and images).

### MongoDB and Flask Application
* app.py- flask app that uses MongoDB to create an html page with scraped info. Two routes: index (queries Mongo database and passes the mars data into an HTML template for display) and scrape (imports scrape_mars.py)
* scrape_mars.py - 'scrape' function that executes all scraping and returns a python dictionary to app.py
* index.html - takes the mars data dictionary and displays all of the data in  HTML elements
* static/styles.css - cascading style sheet describes how HTML elements are to be displayed on screen and varying media

### Usage:

Run app.py in your terminal.  Click on the local host link or copy and paste into your browser.  On the html page, click on the Scrape Mars button to scrape new data.