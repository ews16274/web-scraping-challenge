#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Import dependencies and setup
from bs4 import BeautifulSoup
from splinter import Browser
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager


# In[2]:


#Setting up the driver

executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# # Connect to the Mars News Site

# In[3]:


#Connecting to NASA site
url = "https://mars.nasa.gov/news/"
browser.visit(url)


# In[4]:


# Parse Results HTML with BeautifulSoup
# Find Everything Inside:

html = browser.html
news_soup = BeautifulSoup(html, "html.parser")
slide_element = news_soup.select_one("ul.item_list li.slide")


# In[5]:


slide_element.find("div", class_="content_title")


# In[6]:


# Scrape the Latest News Title
# Use Parent Element to Find First <a> Tag and Save it as news_title
news_title = slide_element.find("div", class_="content_title").get_text()
print(news_title)


# In[7]:


# Scrape the Latest Paragraph Text
news_paragraph = slide_element.find("div", class_="article_teaser_body").get_text()
print(news_paragraph)


# # Finding Space Image From Mars

# In[8]:


# Visit the NASA JPL (Jet Propulsion Laboratory) Site
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)
url = "https://spaceimages-mars.com/"
browser.visit(url)


# In[9]:


# Ask Splinter to Go to Site and Click Button with Class Name full_image
full_image_button = browser.find_by_xpath("/html/body/div[1]/div/a/button")
full_image_button.click()


# In[10]:


# Find "More Info" Button and Click It
#html = browser.html
#more_info_element = browser.find_link_by_partial_text("inspect")
#more_info_element.click()


# In[11]:


# Parse Results HTML with BeautifulSoup
html = browser.html
image_soup = BeautifulSoup(html, "html.parser")


# In[12]:


img_url = image_soup.find(class_="fancybox-image")["src"]
img_url


# In[13]:


# Use Base URL to obtain absolute URL
img_url = f"https://spaceimages-mars.com/{img_url}"
print(img_url)


# # Mars Facts

# In[14]:


# Visit the Mars Facts Site Using Pandas to Read
mars_facts = pd.read_html("https://galaxyfacts-mars.com/")[0]
print(mars_facts)
mars_facts.reset_index(inplace=True)
mars_facts.columns=["ID", "Properties", "Mars", "Earth"]
mars_facts


# # Mars Hemispheres

# In[15]:


# Visit the USGS Astrogeology Science Center Site
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)
url = "https://marshemispheres.com/"
browser.visit(url)


# In[16]:


hemisphere_image_urls = []

# Get a List of All the Hemispheres
links = browser.find_by_css("a.itemLink h3")
for item in range(len(links)):
    hemisphere = {}
    #Find Element on Each Loop to Avoid a Stale Element Exception
    browser.find_by_css("a.itemLink h3").click()
    
    # Find Sample Image Anchor Tag & Extract <href>
    sample_element = browser.find_link_by_text("Sample")
    hemisphere["img_url"] = sample_element["href"]
    
# Get Hemisphere Title
    hemisphere["title"] = browser.find_by_css("h2.title").text
    
#Append Hemisphere Object to List
    hemisphere_image_urls.append(hemisphere)
    
    # Navigate Backwards
    browser.back()


# In[17]:


#Image URLS capture
hemisphere_image_urls


# In[ ]:




