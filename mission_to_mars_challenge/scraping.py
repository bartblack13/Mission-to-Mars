from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd
import datetime as dt

from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager

# Set up Splinter
def scrape_all():
    executable_path = {'executable_path': GeckoDriverManager().install()}
    browser = Browser('firefox', **executable_path, headless=True)
    # changed headless param to True so we don't see the scraping

    news_title, news_paragraph = mars_news(browser)
    hemisphere_url_title = mars_hemispheres(browser)
    # Run all scraping functions and store results in a dictionary
    data = {
        "news_title": news_title,
        "news_paragraph": news_paragraph,
        "featured_image": featured_image(browser),
        "facts": mars_facts(),
        "hemispheres": hemisphere_url_title,
        "last_modified": dt.datetime.now()
    }

    # Stop webdriver and return data
    browser.quit()
    return data

# set up function for repeat scraping
def mars_news(browser):
    
    # Visit the Quotes to Scrape site
    url = 'https://redplanetscience.com'
    browser.visit(url)
    
    # Optional delay for loading the page
    browser.is_element_present_by_css('div.list_text', wait_time=1)

    # Convert the browser html to a soup object and then quit the browser
    # Parse the HTML
    html = browser.html
    news_soup = soup(html, 'html.parser')
    
    # slide_elem = news_soup.select_one('div.list_text')
    # slide_elem.find('div', class_='content_title')

    # # Use the parent element to find the first `a` tag and save it as `news_title`
    # news_title = slide_elem.find('div', class_='content_title').get_text()
    # news_title


    # # use .find_all() instead of .find() when pulling the summary, we would retrieve all of the summaries on the page instead of just the first one
    # # Use the parent element to find the paragraph text
    # # news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
    # # news_p
    # # deleted news_p and put it in return statement
    # return news_title, news_p
    # Add try/except for error handling
    try:
        slide_elem = news_soup.select_one('div.list_text')
        # Use the parent element to find the first 'a' tag and save it as 'news_title'
        news_title = slide_elem.find('div', class_='content_title').get_text()
        # Use the parent element to find the paragraph text
        news_p = slide_elem.find('div', class_='article_teaser_body').get_text()

    except AttributeError:
        return None, None
    
    return news_title, news_p

def featured_image(browser):
    # Visit URL
    url = 'https://spaceimages-mars.com'
    browser.visit(url)

    # Find and click the full image button
    full_image_elem = browser.find_by_tag('button')[1]
    full_image_elem.click()

    # Parse the resulting html with soup
    html = browser.html
    img_soup = soup(html, 'html.parser')

    # Add try/except for error handling
    try:
        # Find the relative image url
        img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')

    except AttributeError:
        return None


    # may not work since there are only 1 images and not a slide show like in the example
    # Find the relative image url
    # img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
    # img_url_rel

    # Use the base URL to create an absolute URL
    img_url = f'https://spaceimages-mars.com/{img_url_rel}'
    # img_url
    return img_url

def mars_facts():
    try:
        # Use 'read_html' to scrape the facts table into a dataframe
        df = pd.read_html('https://galaxyfacts-mars.com')[0]

    except BaseException:
        return None

    # df = pd.read_html('https://galaxyfacts-mars.com')[0]
    # Assign columns and set index of dataframe
    df.columns=['description', 'Mars', 'Earth']
    df.set_index('description', inplace=True)
    # df

    # df.to_html()
    # Convert dataframe into HTML format, add bootstrap
    return df.to_html(classes="table table-striped")

# browser.quit()
# if __name__ == "__main__":

#     # If running as script, print scraped data
#     print(scrape_all())


# # D1: Scrape High-Resolution Mars??? Hemisphere Images and Titles

# ### Hemispheres
def mars_hemispheres(browser):
    # 1. Use browser to visit the URL 
    url = 'https://marshemispheres.com/'

    browser.visit(url)

    # 2. Create a list to hold the images and titles.
    hemisphere_image_urls = []

    # 3. Write code to retrieve the image urls and titles for each hemisphere.
    # Parse the resulting html with soup
    for i in range(4):
        html = browser.html
        img_soup = soup(html, 'html.parser')
        
        image_i_src = img_soup.find_all('div', class_="description")[i].find('a', class_='itemLink product-item').get('href')
    #     image_i_src
        
        # Use the base URL to create an absolute URL
        img_url = f'https://marshemispheres.com/{image_i_src}'
    #     img_url

        browser.visit(img_url)
        
        html = browser.html
        img_soup = soup(html, 'html.parser')
        
        image_sample = img_soup.find_all('div', class_="downloads")[0].find('ul').find('li').a.get('href')
    #     image_sample

        # Use the base URL to create an absolute URL
        sample_url = f'https://marshemispheres.com/{image_sample}'
    #     sample_url

        title_i = img_soup.find_all('h2')[0].get_text()
    #     title_i

        hemispheres = {}
        hemispheres['url'] = sample_url
        hemispheres['title'] = title_i
        hemisphere_image_urls.append(hemispheres)

        browser.back()


    # 4. Print the list that holds the dictionary of each image url and title.
    return hemisphere_image_urls

# # 5. Quit the browser
# browser.quit()

if __name__ == "__main__":

    # If running as script, print scraped data
    print(scrape_all())
