import nextcord
import config 
import os
import io
import json

from nextcord.ext import commands
from nextcord import Interaction, SlashOption, ChannelType, User
from nextcord.abc import GuildChannel
from googleapiclient.discovery import build


intents = nextcord.Intents.all()
intents.members = True

bot = commands.Bot(command_prefix='$', intents=intents)

def on_exit(icon, item):
    icon.stop()

print("$$$$$$$\                  $$\                 $$$$$$$\             $$\  ")   
print("$$  __$$\                 $$ |                $$  __$$\            $$ |    ")
print("$$ |  $$ | $$$$$$\   $$$$$$$ | $$$$$$\        $$ |  $$ | $$$$$$\ $$$$$$\   ")
print("$$$$$$$\ |$$  __$$\ $$  __$$ | \____$$\       $$$$$$$\ |$$  __$$\\\_$$  _|    ")
print("$$  __$$\ $$ /  $$ |$$ /  $$ | $$$$$$$ |      $$  __$$\ $$ /  $$ | $$ |     ")
print("$$ |  $$ |$$ |  $$ |$$ |  $$ |$$  __$$ |      $$ |  $$ |$$ |  $$ | $$ |$$\ ")
print("$$$$$$$  |\$$$$$$  |\$$$$$$$ |\$$$$$$$ |      $$$$$$$  |\$$$$$$  | \$$$$  |")
print("\_______/  \______/  \_______| \_______|      \_______/  \______/   \____/")
print("                                                                          ")
print("   __         ___      __ __      ")
print(" /'__`\     /'___`\   /\ \\\ \   ")
print("/\ \/\ \   /\_\ /\ \  \ \ \\\ \     ")
print("\ \ \ \ \  \/_/// /__  \ \ \\\ \_  ")
print(" \ \ \_\ \__  // /_\ \__\ \__ ,__\ ")
print("  \ \____/\_\/\______/\_\\\/_/\_\_/")
print("   \/___/\/_/\/_____/\/_/   \/_/")
print("                                   ")
print("@afonsosr1v\n")


if os.path.exists("keys.json") and os.access("keys.json", os.R_OK):
    print("Keys were found, starting bot...")
    with open('keys.json') as json_file:  

        keys = json.load(json_file)

    config.TOKEN = keys['bot_token']
    config.GOOGLESEARCHAPI = keys['google_search_api']
    config.CX = keys['google_cx']
    config.SERVERID = int(keys['server_id'])

else:
    print("Keys were not found, creating keys.json...")
    print("Please input the following keys: \n")

    keys = {  
        'bot_token': input('Bot Token: '),
        'google_search_api': input('Google Search API: '),
        'google_cx': input('Google CX: '),
        'server_id': input('Server ID: '),
    }

    with open('keys.json', 'w') as outfile:  
        json.dump(keys, outfile)
    
    config.TOKEN = keys['bot_token']
    config.GOOGLESEARCHAPI = keys['google_search_api']
    config.CX = keys['google_cx']
    config.SERVERID = int(keys['server_id'])






@bot.event
async def on_ready():
    print("888888ba             dP      .d88888b    dP                       dP                  dP ")
    print("88    `8b            88      88.    ''   88                       88                  88 ")
    print("a88aaaa8P .d8888b. d8888P    `Y88888b. d8888P .d8888b. 88d888b. d8888P .d8888b. .d888b88 ")
    print("88   `8b. 88'  `88   88            `8b   88   88'  `88 88'  `88   88   88ooood8 88'  `88 ")
    print("88    .88 88.  .88   88      d8'   .8P   88   88.  .88 88         88   88.  ... 88.  .88 ")
    print("88888888P `88888P'   dP       Y88888P    dP   `88888P8 dP         dP   `88888P' `88888P8")
    print("                                     ")
    print(f'{bot.user.name} - ID: {(bot.user.id)}')
    print('*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*')



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