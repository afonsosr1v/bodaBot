import nextcord
from nextcord.ext import commands


class Cmds(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def test(self, ctx):
        await ctx.send("drena drena drena")

    # @commands.Cog.listener
    # async def on_member_join(self, member):
    #    guild = member.guild
    #   channel_id = 790904854104113173
    #    channel = guild.get_channel(channel_id)

    #    if channel:
    #        embed = nextcord.Embed(
    #            title = "Xe Wi",
    #            description=f"Onde é q tu pensas q vais {member.mention}?",
    #           color=nextcord.Color.red()
    #        )
    #       embed.set_thumbnail(url=member.avatar_url) 
   

def setup(bot):
    bot.add_cog(Cmds(bot))