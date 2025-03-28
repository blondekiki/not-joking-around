import discord
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Get the Discord bot token from the environment
TOKEN = os.getenv('DISCORD_TOKEN')

# Create an instance of the Client
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

# Event: When the bot has connected to Discord
@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

# Event: When a message is received in a server
@client.event
async def on_message(message):
    # Avoid the bot replying to its own messages
    if message.author == client.user:
        return

    # Respond to a command
    if message.content.startswith('!hello'):
        await message.channel.send('Hello!')

# Start the bot with the token from the .env file
client.run(TOKEN)
