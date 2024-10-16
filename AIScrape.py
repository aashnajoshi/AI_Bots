import streamlit as st
from playwright.sync_api import sync_playwright
import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv('GPT_API_KEY')

st.title("AI Web Scraper")
url = st.text_input("Enter the URL of the website you want to scrape:")
prompt = st.text_area("Describe your filter (e.g., 'select all black dresses under 5000'):")

if url and prompt:
    st.write("Scraping website...")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(url)
        products = page.locator('.product-class').all_text_contents()
        prices = page.locator('.price-class').all_text_contents()
        links = page.locator('.link-class').all_inner_texts()
        scraped_data = [{'name': p, 'price': pr, 'link': l} for p, pr, l in zip(products, prices, links)]
        browser.close()

    gpt_prompt = f"From this list: {scraped_data}, {prompt}"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=gpt_prompt,
        max_tokens=500)
    
    filtered_output = response.choices[0].text.strip()
    st.write("Filtered Results:")
    st.write(filtered_output)
