from kindwise import PlantApi, PlantIdentification, UsageInfo
from dotenv import load_dotenv
import os
from tkinter import Tk
from tkinter.filedialog import askopenfilename

load_dotenv()

def identify_plant(image_path):
    api = PlantApi(api_key=os.getenv("PLANT_API"))
    try:
        usage: UsageInfo = api.usage_info()
        identification: PlantIdentification = api.identify(image_path)
        identification_with_different_views: PlantIdentification = api.get_identification(identification.access_token)
        api.delete_identification(identification)
        return identification_with_different_views  # Return the plant identification data
        
    except Exception as e:
        print(f"Error identifying plant: {e}")
        return None

def print_plant_info(plant_data):
    if plant_data:
        print(f"Plant Name: {plant_data.common_name}")
        print(f"Scientific Name: {plant_data.scientific_name}")
        print(f"Other Info: {plant_data.additional_info}")
    else:
        print("No plant data available.")

def main():
    Tk().withdraw()
    image_path = askopenfilename(title="Select a Plant Image", filetypes=[("Image Files", "*.jpg"), ("Image Files", "*.jpeg"), ("Image Files", "*.png"), ("Image Files", "*.bmp")])
    if image_path:
        plant_data = identify_plant(image_path)
        print_plant_info(plant_data)
    else:
        print("No file selected.")

if __name__ == "__main__":
    main()
