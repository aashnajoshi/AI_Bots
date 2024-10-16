# AI Bots
A compilation of AI-powered bots that use APIs for various platforms, such as Discord, Telegram, YouTube, and more. These bots perform tasks ranging from generating text responses and images to summarizing YouTube videos and identifying plant species.

## Features
- GPT-based conversational agents for console, Discord, Telegram, etc.
- YouTube video transcript summarization and Q&A.
- Image generation based on text prompts.
- Plant identification using image inputs.

## Usage
### All required libraries can be installed using a single-line command:
```bash
pip install -r requirements.txt
```
### While to run the code:
```bash
  python {file_name}.py
```
## Description about various files:
- **.env:** Contains all the credentials and secret information.
- **AIScrape.py:** An AI-based Webscrapper that takes url and prompt from user to customize the webscrapping process as per need.
- **Console_GPT:** An interactive command-line assistant that provides text responses or generates images based on user prompts.
- **Discord_GPT:** A discord chatbot that responds to user messages with text replies or generates images based on prompts when mentioned in a channel.
- **GenAI_Model:** A notebook exploring text generation and image creation using AI models.
- **ImageGen:** A command-line tool that generates images based on user prompts and saves them with dynamically created filenames.
- **Telegram_GPT:** A telegram chatbot that responds to user messages with AI-generated answers, initiated by a simple command.
- **Youtube_GPT:** A tool that retrieves video transcripts from YouTube, generates a summary using AI, and answers user questions about the video content.
- **Plant_ID:** A desktop application that identifies plants from images using an API and displays relevant information about the identified species.
- **requirements.txt:**  File containing all required Python modules.
