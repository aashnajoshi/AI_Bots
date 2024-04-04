import openai
import discord
from dotenv import load_dotenv
import os

load_dotenv()
openai.api_key = os.getenv("GPT_API_KEY")

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        if message.author == self.user:  # Ignore messages from bot
            return
        if self.user in message.mentions:  # Check bot mention
            await self.handle_input(message)

    async def handle_input(self, message):
        user_input = message.content.replace(f'<@!{self.user.id}>', '').strip()  # Remove bot mention
        if any(greeting in user_input.lower() for greeting in ["hi", "hello", "hey", "greetings"]):
            await message.channel.send(f"Hello {message.author.mention}! I am a Work-In-Progress GPT Bot!")
            return
        if any(keyword in user_input.lower() for keyword in ["draw", "imagine", "generate", "create"]):
            await self.image_generator(message.channel, user_input, message.author.mention)
        else:
            await self.chatbot(message.channel, user_input)

    async def chatbot(self, channel, user_input):
        response = self.ask_gpt(user_input, "text")
        await channel.send(response)

    async def image_generator(self, channel, user_input, msg):
        response = self.ask_gpt(user_input, "image")
        await channel.send(f"Here's an image link to \"{user_input}\":\n{response}")

    def ask_gpt(self, user_input, model_type):
        if model_type == "text":
            response = openai.Completion.create(prompt=user_input, model="gpt-3.5-turbo-instruct", max_tokens=150,)
            return response.choices[0].text.strip()
        elif model_type == "image":
            response = openai.Image.create(prompt=user_input, n=1, size="1024x1024", quality="standard",  model="dall-e-3")
            return response['data'][0]['url']

intents = discord.Intents.default()
intents.messages = True

client = MyClient(intents=intents)
client.run(os.getenv("DISCORD_TOKEN"))