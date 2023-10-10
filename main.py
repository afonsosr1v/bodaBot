import nextcord
import config 
import config_menu
import os
from nextcord.ext import commands
from nextcord import Interaction, SlashOption, ChannelType, User
from nextcord.abc import GuildChannel
from googleapiclient.discovery import build

intents = nextcord.Intents.all()
intents.members = True

bot = commands.Bot(command_prefix='$', intents=intents)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} {(bot.user.id)}')
    print('------')


#Load Cogs
#for filename in os.listdir('./cogs'):
#    if filename.endswith('.py'):
#    bot.load_extension(f'cogs.{filename[:-3]}')


@bot.slash_command(name="ping", description="Pinga de Volta para Teste", guild_ids=[config.SERVERID])
async def ping(interaction: nextcord.Interaction):
    await interaction.response.send_message("Ping")

@bot.slash_command(guild_ids=[config.SERVERID], name="review", description="Comando para Review de Albuns")
async def echo(
    interaction: nextcord.Interaction,
    artista: str,
    album: str,
    nota: int,
    opinião: str):
    print(f"```\n{artista} - {album} \n Opinião: {opinião} \n Nota: {nota}/10 \n User: {interaction.user}\n```")
    embed = nextcord.Embed(
        title= f"{artista} - {album}",
        description= f"{opinião}",
        color = nextcord.Color.red()
    )
    resource = build("customsearch", "v1", developerKey=config.GOOGLESEARCHAPI).cse()
    result = resource.list(q=f"{artista} {album}", cx=config.CX, searchType="image").execute()
    img_link = result['items'][0]['link']
    
    embed.set_image(url=img_link) #Dar set da capa do album '''
    embed.add_field(name="Review", value=f"{nota}/10")
    embed.add_field(name="Reviewer", value=interaction.user)
    await interaction.response.send_message(embed=embed)


bot.run(config.TOKEN)   