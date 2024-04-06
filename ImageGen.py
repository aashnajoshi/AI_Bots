import requests
import dotenv
import os
import re

dotenv.load_dotenv()

def generate_filename(prompt):
    # Use regex to extract relevant keywords from the prompt
    keywords = re.findall(r'\b\w{3,}\b', prompt.lower())
    if keywords:
        return keywords[0]
    else:
        return "generated_image"

while True:
    prompt = input("Describe the image you want to be generated: ")
    
    response = requests.post(f"https://api.stability.ai/v2beta/stable-image/generate/core", headers={"authorization": os.getenv("STABILITY_API_KEY"), "accept": "image/*"}, files={"none": ''}, data={"prompt": prompt, "output_format": "webp",},)

    if response.status_code == 200:
        filename = generate_filename(prompt)
        with open(f"./{filename}.webp", 'wb') as file:
            file.write(response.content)
    else:
        raise Exception(str(response.json()))

    choice = input("Do you want to explore the bot further? (Y/N): ")
    if choice.upper() != 'Y':
        break