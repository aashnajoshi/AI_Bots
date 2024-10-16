from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import streamlit as st
import openai
import os

load_dotenv()

def scrape_website(url):
    chrome_options = Options()
    chrome_options.add_argument('--headless')  # Run in headless mode for no GUI
    service = Service(executable_path='C:/chromedriver/chromedriver.exe')  # Update this path
    driver = webdriver.Chrome(service=service, options=chrome_options)
    try:
        driver.get(url)
        products = [elem.text for elem in driver.find_elements(By.CLASS_NAME, 'product-class')]
    except Exception as e:
        products = [str(e)]
    finally:
        driver.quit()
    return products

st.title('AI Scrape')
url = st.text_input('Enter URL to scrape')

if st.button('Scrape'):
    if url:
        scraped_data = scrape_website(url)
        st.write('Scraped Data:')
        st.write(scraped_data)
    else:
        st.error('Please enter a valid URL.')
