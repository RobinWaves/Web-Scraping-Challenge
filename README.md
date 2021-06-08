# Web-Scraping-Challenge

## Mission to Mars
***

This assignment builds a web application that scrapes various websites for data related to the Mission to Mars and displays the information in a single HTML page.

### Scraping
* mission_to_mars.ipynb - scraping and analysis of NASA Mars News (title and short paragraph), JPL Mars Space Images (featured image), Mars Facts (table), Mars Hemishpere (titles and images).

### MongoDB and Flask Application
* app.py- flask app that uses MongoDB to create an html page with scraped info. Two routes: inde (queries Mongo database and pass the mars data into an HTML template for display) and scrape (imports scrape_mars.py)
* scrape_mars.py - 'scrape' function that executes all scraping and returns a python dictionary to app.py
* index.html - html page containing scraped info
* static/styles.css


* Create a root route `/` that will query your Mongo database and pass the mars data into an HTML template to display the data.

* Create a template HTML file called `index.html` that will take the mars data dictionary and display all of the data in the appropriate HTML elements. Use the following as a guide for what the final product should look like, but feel free to create your own design.

![final_app_part1.png](Images/final_app.png)

- - -

## Step 3 - Submission

To submit your work to BootCampSpot, create a new GitHub repository and upload the following:

1. The Jupyter Notebook containing the scraping code used.

2. Screenshots of your final application.

3. Submit the link to your new repository to BootCampSpot.

4. Ensure your repository has regular commits (i.e. 20+ commits) and a thorough README.md file

## Hints

* Use Splinter to navigate the sites when needed and BeautifulSoup to help find and parse out the necessary data.

* Use Pymongo for CRUD applications for your database. For this homework, you can simply overwrite the existing document each time the `/scrape` url is visited and new data is obtained.

* Use Bootstrap to structure your HTML template.

## Rubric

[Unit 12 Rubric - Web Scraping Homework - Mission to Mars](https://docs.google.com/document/d/1paGEIFS5yp2VQu6G8F45B4uj1t1t29zL73KEQrD0xpo/edit?usp=sharing)

- - -

© 2021 Trilogy Education Services, LLC, a 2U, Inc. brand. Confidential and Proprietary. All Rights Reserved.
