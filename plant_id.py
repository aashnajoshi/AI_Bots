from kindwise import PlantApi, PlantIdentification, UsageInfo
from dotenv import load_dotenv
import os
from tkinter import Tk
from tkinter.filedialog import askopenfilename

load_dotenv()

def identify_plant(image_path):
    api = PlantApi(api_key= os.getenv("PLANT_API"))

    # Logic to identify plant from the url and name (TBM)
    usage: UsageInfo = api.usage_info()
    identification: PlantIdentification = api.identify(image_path)
    identification_with_different_views: PlantIdentification = api.get_identification(identification.access_token)
    api.delete_identification(identification)

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