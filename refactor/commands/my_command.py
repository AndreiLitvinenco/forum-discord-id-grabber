import discord
from discord import app_commands
from discord.ext import commands

async def setup(bot: commands.Bot):
    @app_commands.command(name="mycommand", description="This is a slash command")
    async def my_command(interaction: discord.Interaction):
        await interaction.response.send_message("Hello World from a separate file!")

    bot.tree.add_command(my_command)
