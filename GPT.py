import openai # openai==0.28
from dotenv import load_dotenv #python-dotenv
import os

load_dotenv()
openai.api_key = os.getenv("GPT_API_KEY")

def handle_input(prompt, model_type):
    while True:
        user_input = input(prompt)
        if any(greeting in user_input.lower() for greeting in ["hi", "hello", "hey", "hi there", "hello there"]):
            print("Bot: Hello! How can I help you?")
            continue

        if model_type == "text":
            response = openai.Completion.create(prompt=user_input, model="gpt-3.5-turbo-instruct", max_tokens=150,)
            print("Bot:", response.choices[0].text.strip(), "\n")
            
        elif model_type == "image":
            response = openai.Image.create(prompt=user_input, n=1)
            print(f"Here's an image link to \"{user_input}\"\n\n",response['data'][0]['url'])

        further_question = input("Do you want to explore the bot further? (Y/N): ").capitalize()
        while further_question not in {"Y", "N"}:
            further_question = input("Please enter 'Y' for Yes or 'N' for No.")

        if further_question == "N":
            print("Thank you for using our service. Goodbye!")
            break

def chatbot():
    print("Welcome! How can I assist you today?")
    handle_input("You: ", "text")

def image_generator():
    handle_input("Describe the image you want to be generated: ", "image")

# Main menu
while True:
    choice = input("Choose an option:\n1. Answer your query\n2. Draw an image based on a prompt\n3. Exit\nYour choice: ")
    if choice == "1":
        chatbot()
    elif choice == "2":
        image_generator()
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please choose again.")