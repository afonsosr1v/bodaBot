import nextcord
import tokens 
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
print("   __      ______      _      ")
print(" /'__`\   /\  ___\   /' \    ")
print("/\ \/\ \  \ \ \__/  /\_, \   ")
print("\ \ \ \ \  \ \___``\\\/_/\ \  ")
print(" \ \ \_\ \__\/\ \L\ \__\ \ \  ")
print("  \ \____/\_\\\ \____/\_\\\ \_\\")
print("   \/___/\/_/ \/___/\/_/ \/_/")
print("                                   ")
print("@afonsosr1v\n @Grd100000\n")


if os.path.exists("keys.json") and os.access("keys.json", os.R_OK):
    print("Keys were found, starting bot...")
    with open('keys.json') as json_file:  

        keys = json.load(json_file)

    tokens.TOKEN = keys['bot_token']
    tokens.GOOGLESEARCHAPI = keys['google_search_api']
    tokens.CX = keys['google_cx']
    tokens.SERVERID = int(keys['server_id'])

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
    
    tokens.TOKEN = keys['bot_token']
    tokens.GOOGLESEARCHAPI = keys['google_search_api']
    tokens.CX = keys['google_cx']
    tokens.SERVERID = int(keys['server_id'])






@bot.event
async def on_ready():
    print('*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.')
    print("                                                          ")
    print(" ___   ___  _____      ___   _      _     _   _      ____ ")
    print("| |_) / / \  | |      / / \ | |\ | | |   | | | |\ | | |_  ")
    print("|_|_) \_\_/  |_|      \_\_/ |_| \| |_|__ |_| |_| \| |_|__ ")
    print("                                                          ")
    print(f'{bot.user.name} - ID: {(bot.user.id)}')
    print('*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.')




#Load Cogs
#for filename in os.listdir('./cogs'):
#    if filename.endswith('.py'):
#    bot.load_extension(f'cogs.{filename[:-3]}')


@bot.slash_command(name="ping", description="Pinga de Volta para Teste", guild_ids=[tokens.SERVERID])
async def ping(interaction: nextcord.Interaction):
    await interaction.response.send_message("Ping")

@bot.slash_command(guild_ids=[tokens.SERVERID], name="review", description="Comando para Review de Albuns")
async def speak(
    interaction: Interaction,
    artista: str,
    album: str,
    opinião: str,
    nota: int = SlashOption(
        name="nota",
        choices={"0/10": 0. "1/10": 1, "2/10": 2, "3/10": 3, "4/10": 4, "5/10": 5, "6/10": 6, "7/10": 7, "8/10": 8, "9/10": 9, "10/10": 10},
        ),
    ):
    
    print(f"```\n{artista} - {album} \n Opinião: {opinião} \n Nota: {nota}/10 \n User: {interaction.user}\n```")

    embed = nextcord.Embed(
        title= f"{artista} - {album}",
        description= f"{opinião}",
        color = nextcord.Color.red()
    )
    
    resource = build("customsearch", "v1", developerKey=tokens.GOOGLESEARCHAPI).cse()
    result = resource.list(q=f"{artista} {album}", cx=tokens.CX, searchType="image").execute()
    img_link = result['items'][0]['link']
    
    embed.set_image(url=img_link) #Dar set da capa do album '''
    embed.add_field(name="Review", value=f"{nota}/10")
    embed.add_field(name="Reviewer", value=interaction.user)
    await interaction.response.send_message(embed=embed)

bot.run(tokens.TOKEN)   