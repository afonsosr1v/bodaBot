import nextcord
import config 
import coverpy
import os
from nextcord.ext import commands
from nextcord import Interaction, SlashOption, ChannelType, User
from nextcord.abc import GuildChannel

intents = nextcord.Intents.all()
intents.members = True
server_id = 688100174433878081

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} {(bot.user.id)}')
    print('------')

#Load Cogs
#for filename in os.listdir('./cogs'):
#    if filename.endswith('.py'):
#        bot.load_extension(f'cogs.{filename[:-3]}')


@bot.slash_command(name="ping", description="Pinga de Volta para Teste", guild_ids=[server_id])
async def ping(interaction: nextcord.Interaction):
    await interaction.response.send_message("Ping")

@bot.slash_command(guild_ids=[server_id], name="review", description="Comando para Review de Albuns")
async def embed_create(
    interaction: nextcord.Interaction,
    artista: str,
    album: str,
    nota: int,
    opinião: str):
    #await interaction.response.send_message(f"```{artista} - {album} \n Opinião: {opinião} \n Nota: {nota}/10 \n User: {interaction.user}```")
    embed = nextcord.Embed(
        title= f"{artista} - {album}",
        description= f"Opinião: {opinião}",
        color = nextcord.Color.red()
    )
    limit=1
    result = coverpy.get_cover(album, limit)
    embed.set_thumbnail(url=result)
    embed.add_field(name="Review", value=f"{nota}/10")
    embed.add_field(name="Reviewer", value=interaction.user)
    await interaction.response.send_message(embed=embed)

    


bot.run(config.TOKEN)   