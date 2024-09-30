import requests
from dotenv import load_dotenv
import os
from tkinter import Tk
from tkinter.filedialog import askopenfilename

load_dotenv()

def identify_plant(image_path):
    api_key = os.getenv("PLANT_API")
    url = os.getenv("PLANT_URL")

    # Logic to identify plant from the url and name

def print_plant_info(plant_data):
    if 'suggestions' in plant_data and len(plant_data['suggestions']) > 0:
        suggestion = plant_data['suggestions'][0]
        print("Scientific Name:", suggestion['scientific_name'])
        print("Common Name:", suggestion['common_names'])
        
        if 'medicinal_uses' in suggestion and suggestion['medicinal_uses']:
            print("Medicinal Uses:", suggestion['medicinal_uses'])
        else:
            print("No medicinal uses found.")
    else:
        print("No plant identified.")

def main():
    Tk().withdraw()
    image_path = askopenfilename(title="Select a Plant Image", filetypes=[("Image Files", "*.jpg;*.jpeg;*.png;*.bmp")])
    
    if image_path:
        plant_data = identify_plant(image_path)
        print_plant_info(plant_data)
    else:
        print("No file selected.")

if __name__ == "__main__":
    main()