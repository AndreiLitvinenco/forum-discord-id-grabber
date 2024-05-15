import discord
from discord import app_commands
from discord.ext import commands
import os 
from dotenv import load_dotenv
load_dotenv()


Client = commands.Bot(command_prefix="/", intents = discord.Intents.all())

@Client.event
async def on_ready():
    print("Bot is ready")
    try:
        synced = await Client.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(e)

@Client.tree.command(name='hello')
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message(f'Hey {interaction.user.mention}! This is a slash command.', ephemeral=True)
    print(f'hello command executed by {interaction.user.mention}')

@Client.tree.command(name='say', description='Test')
@app_commands.describe(arg = 'What should I say?')
async def say(interaction: discord.Interaction, arg: str):
    await interaction.response.send_message(f'{interaction.user.name} said: `{arg}`')

@Client.tree.command(name = 'userinfo')
async def userinfo(interaction: discord.Interaction, member:discord.Member):
    embed = discord.Embed(title= 'User info', description= f'Here is the user info on {member.name}', color= discord.Color.green())
    await interaction.response.send_message(embed=embed, ephemeral=True)


Client.run(os.getenv('discord_token'))