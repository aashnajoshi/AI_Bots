from googleapiclient.discovery import build
import openai
from dotenv import load_dotenv
import os

load_dotenv()
openai.api_key = os.getenv("GPT_API_KEY")
youtube_api_key = os.getenv("YOUTUBE_API_KEY")

youtube = build('youtube', 'v3', developerKey=youtube_api_key) # Set up YouTube Data API v3

def get_video_transcript(video_id):
    request = youtube.captions().list(part='snippet', videoId=video_id)
    response = request.execute()

    if 'items' in response:
        for item in response['items']:
            if item['snippet']['trackKind'] == 'standard':
                caption_id = item['id']
                caption_request = youtube.captions().download(id=caption_id, tfmt='srt')
                caption_response = caption_request.execute()
                return caption_response.decode('utf-8')
                
    return None

def generate_summary(text):
    response = openai.Completion.create(engine="text-davinci-003", prompt=text, max_tokens=150, temperature=0.7, n=1)
    return response.choices[0].text.strip()

def main():
    video_link = input("Enter the YouTube video link: ")
    video_id = video_link.split("=")[-1]
    transcript = get_video_transcript(video_id)

    if transcript:
        summary = generate_summary(transcript)
        print(f"\nThe video is about: {summary}")

        while True:
            question = input("What do you want to know about the video? (If Nothing press 'N' else enter the question): ")

            if question.lower() == "n":
                break
            answer = generate_answer(question, summary)
            print(answer)
    else:
        print("Unable to retrieve transcript for the video.")

if __name__ == "__main__":
    main()