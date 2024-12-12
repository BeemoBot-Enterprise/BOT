import discord
from discord import app_commands
from Logs.logs import command_used
from Riot.riot_api import *
import typing

def setup_global_commands(bot):
    # Define a slash command
    @bot.tree.command(name="hello", description="Say hello!")
    async def hello(interaction: discord.Interaction):
        command_used("hello", interaction.user)
        await interaction.response.send_message("Hello! 👋")

    @bot.tree.command(name="ping", description="Check the bot's latency")
    async def ping(interaction: discord.Interaction):
        command_used("ping", interaction.user)
        await interaction.response.send_message(f"Pong! 🏓 ({bot.latency * 1000:.0f}ms)")

    @bot.tree.command(name="user",
                description="get basic rank infos")
    @app_commands.describe(name="The summoner name")
    async def user(interaction: discord.Interaction, name: str):
        command_used("user", interaction.user)
        await interaction.response.send_message(get_summoner_by_puuid(get_puuid_by_name(name)))
        # Add more commands here if needed
