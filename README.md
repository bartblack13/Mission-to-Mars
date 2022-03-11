# Mission-to-Mars
MongoDB, Flask, BeautifulSoup, Splinter, HTML and CSS

## Purpose
The purpose of this exercise was to gain experience with html tags (specifically by scraping), using MongoDB, Flask, BeautifulSoup, Splinter, and HTML and CSS (to develop an app). To accomplish this task I helped a mock friend develop an app/website offered news and data regarding Mars Exploration (See Figure 1)  I used the following tools and techniques:
* GeckoManagerDriver for Firefox and developer tools to identify HTML components attached to the desired data
* Beautiful Soup and Splinter to automate scrape (automate a web browser) and gather the desired data 
* Mongo, a no SQL database, to store data;
* Flask to create a web application to display data

## Method
To do this I wrote pythonic code using jupyter notebook to scrape data and pictures from various websites, which could then be used for my own app.  The code was then exported as a python file and cleaned up, so it could be used as my scraping.py file.  The scraping.py file was linked to my app.py file, which held the routes for the website.  I also wrote a basic html index file (index.html). The website included Bootstrap components such as: 
* jumbotron and a interactive scrape button, 
* tables,
* grid layout for titles, etc. (see Figure 1)<br><br>
![This is an image](https://github.com/bartblack13/Mission-to-Mars/blob/main/Resources/website.png)<br><br>
**Figure 1 - Website screenshot** <br><br>

The Jumbotron included an interactive button for users to scrape new up-to-date data, info, and featured images.  This generated the data included in the Mars Facts table; the Feature image, title, and summary; and the four hemisphere images with corresponding names.

As deiverables for this challenge I did the following: 

* Deliverable 1: Scrape Full-Resolution Mars Hemisphere Images and Titles
* Deliverable 2: Update the Web App with Mars Hemisphere Images and Titles
* Deliverable 3: Add Bootstrap 3 Components
  1) Changed the Scrape button to show "active status" with a color change and shadowing, color change was default and is difficult to see, but is present (see Figure 2)<br><br>
![This is an image](https://github.com/bartblack13/Mission-to-Mars/blob/main/Resources/button%20active.png)<br><br>
**Figure 2 - unactive and active button with code** <br><br>
  2) Updated the Jumbotron with an image (see Figure 3); I tried using a saved image in my static folder to update the jumbrotron, but was unsuccessful.  An image of the code for the static folder can be seen in the resources folder. <br><br>
![This is an image](https://github.com/bartblack13/Mission-to-Mars/blob/main/Resources/jumbotron%20code.png)<br><br>
**Figure 3 - code for jumbotron image** <br><br>
  3) verified that my app was formatted for a mobile device (Samsung S5) (see Figure 4)<br><br>
![This is an image](https://github.com/bartblack13/Mission-to-Mars/blob/main/Resources/mobile%20app.png)<br><br>
**Figure 4 - mobile format of website** <br><br>
