import discord
from discord import app_commands
from discord.ext import commands
from forum_functions import *
import os
from dotenv import load_dotenv
load_dotenv()

async def setup(bot: commands.Bot):
    @app_commands.command(name="verify", description="Verify command")
    async def verify(interaction: discord.Interaction):
        await interaction.response.defer()
        data = read_json()
        officer_name = interaction.user.display_name
        identifier = "4263"

        #print(officer_name, identifier)
        driver = setup_driver()
        login(driver, os.getenv('user'), os.getenv('password'))
        profile_url = search_profile(driver, officer_name, identifier)
        roles = get_roles(driver, profile_url)
        discord_id = get_discord_id(driver, profile_url)

        print("Roles:", roles)
        print("Discord ID:", discord_id)
        print("User profile:", profile_url)

        new_data = {officer_name:{
            "id": discord_id,
            "url": profile_url}}
        write_json(data, new_data)

        print(f"discord-id-id = {interaction.user.id}")
        await interaction.followup.send(f"# PROFILE VERIFIED \n{interaction.user.mention} Welcome to the Los Santos Police Department Discord Server, (**Senior Administrative Clerk I Stella Roberts**) \n")

    bot.tree.add_command(verify)
