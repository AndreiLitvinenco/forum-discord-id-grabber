import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
load_dotenv()

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.slash_command(name="userinfo", description="Display userinfo of a user")
async def userinfo(ctx, user: discord.User):
    embed = discord.Embed(title="User Info", description=f"Here is the userinfo for {user.name}", color=0x7289DA)
    embed.set_thumbnail(url=user.avatar_url)
    embed.add_field(name="Username", value=user.name, inline=True)
    embed.add_field(name="Discriminator", value=user.discriminator, inline=True)
    embed.add_field(name="ID", value=user.id, inline=True)
    embed.add_field(name="Avatar URL", value=user.avatar_url, inline=False)
    await ctx.send(embed=embed)

bot.run(os.getenv('discord_token'))
