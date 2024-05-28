from dotenv import load_dotenv
import os
import asyncio
import discord
from discord.ext import commands


intents = discord.Intents.all()
bot = commands.Bot(command_prefix='/', intents=intents)
tree = bot.tree

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(f"Failed to sync commands: {e}")

async def load_extensions():
    for filename in os.listdir('./commands'):
        if filename.endswith('.py'):
            await bot.load_extension(f'commands.{filename[:-3]}')

async def main():
    async with bot:
        await load_extensions()
        await bot.start(os.getenv('discord_token'))


if __name__ == '__main__':
    load_dotenv()
    asyncio.run(main())

