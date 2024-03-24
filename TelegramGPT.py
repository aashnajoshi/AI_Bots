import openai
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from dotenv import load_dotenv
import os

load_dotenv()

openai.api_key = "GPT_API_KEY"

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hello! I am a Work-In-Progress GPT Bot!")

def reply_message(update, context):
    question = update.message.text
    context.bot.send_chat_action(chat_id=update.effective_chat.id, action="typing")  # Show typing indicator
    response = ask_gpt(question)
    context.bot.send_message(chat_id=update.effective_chat.id, text=response)

def ask_gpt(question):
    try:
        prompt = f"Question: {question}\nAnswer:"
        response = openai.Completion.create(prompt=prompt, model="gpt-3.5-turbo-instruct", max_tokens=150)
        return response.choices[0].text.strip()
    except Exception as e:
        return f"An error occurred: {e}"

def main():
    # Create the Updater and pass it your bot's token.
    updater = Updater(token='TG_TOKEN', use_context=True)
    dp = updater.dispatcher

    # Define handlers
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, reply_message))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()