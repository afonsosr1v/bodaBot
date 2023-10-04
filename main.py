import nextcord
import config 
import os
from nextcord.ext import commands
from nextcord import Interaction, SlashOption, ChannelType, User
from nextcord.abc import GuildChannel
from googleapiclient.discovery import build
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

intents = nextcord.Intents.all()
intents.members = True
SCOPES = ['https://googleapis.com/auth/spreadsheets']

#gis = GoogleImagesSearch(config.GOOGLESEARCHAPI, config.CX)

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} {(bot.user.id)}')
    print('------')
    '''credentials = None
    if os.path.exists("token.json"):
        credentials = Credentials.from_authorized_user_file("token.json", SCOPES)
    if not credentials or not credentials.valid:
        if credentials and credentials.expired and credentials.refresh_token:
            credentials.refresh(Request())
        else:  
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
            credentials = flow.run_local_server(port=0)
        with open("token.json", "w") as token:
            token.write(credentials.to_json())

    try:
        service = build("sheets", "v4", credentials=credentials)
        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=config.SHEET_ID, range="Dados!B3:G200").execute()
        values = result.get("values", [])

        for row in values:
            print(values)
    except HttpError as error:
        print(f"An error occured: {error}") '''

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
    #await interaction.response.send_message(f"```{artista} - {album} \n Opinião: {opinião} \n Nota: {nota}/10 \n User: {interaction.user}```")
    embed = nextcord.Embed(
        title= f"{artista} - {album}",
        description= f"{opinião}",
        color = nextcord.Color.red()
    )
    #Pesquisa da capa do album, n estpi a conseguir fazer funcionar
    resource = build("customsearch", "v1", developerKey=config.GOOGLESEARCHAPI).cse()
    result = resource.list(q=f"{artista} {album}", cx=config.CX, searchType="image").execute()
    img_link = result['items'][0]['link']
    
    embed.set_image(url=img_link) #Dar set da capa do album '''
    embed.add_field(name="Review", value=f"{nota}/10")
    embed.add_field(name="Reviewer", value=interaction.user)
    await interaction.response.send_message(embed=embed)


    


bot.run(config.TOKEN)   