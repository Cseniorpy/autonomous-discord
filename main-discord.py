from discord.ext import commands 
from datetime import datetime 
import discord
import time 
import random 
import asyncio 
import numpy

#SELF-MODULES
#from channelapprove import channel_approve


bot = commands.Bot(command_prefix='.')
TOKEN = ('NjI3ODEwODQ1OTcxMzE2NzM3.XZCEjA.b_EOm9IXD6xXJmrHW7-S1rM6TQk')
bot.remove_command('help')



#--------------------------- INFORMATION SECTION ---------------------------#
#                                                                           #
#---------------------------------------------------------------------------#







#------------------------------ EVENT SECTION ------------------------------#
#                                                                           #
#---------------------------------------------------------------------------#

@bot.event
async def on_ready():
    

#----------------------------GLOBAL VARIABLES-------------------------------#
#                                                                           #
#---------------------------------------------------------------------------#
    global public_channel_list
    global channel_bot_test, channel_private_experiments
    channel_bot_test = bot.get_channel(627807374736097310)
    channel_private_experiments = bot.get_channel(627815214422687754)
    public_channel_list = [channel_bot_test,channel_private_experiments]


    print("BOT is ready!")


@bot.event 
async def on_member_join(member):

    channel = bot.get_channel(627812771450454046)
    await channel.send("**Hoşgeldin {} :smile:**".format(member.mention))


@bot.event 
async def on_member_remove(member):

    channel = bot.get_channel(627812771450454046)
    await channel.send("{} Ayrıldı..".format(member.mention))



#------------------------------ COMMAND SECTION ------------------------------#
#                                                                             #
#-----------------------------------------------------------------------------#



@bot.command()
async def yardım(ctx):


    
    if not ctx.channel in public_channel_list:
        await ctx.channel.send("**Bu kanalı kullanmalısın :point_right: {0.mention}**".format(channel_bot_test))

    else:
      
        embed = discord.Embed(title='**YARDIMCI KOMUTLAR**', description='', color=0x4ad7ed)

        embed.add_field(name='**> kanal**', value='```Sunucuda bulunan kanalların açıklamasını gösterir```')
        #embed.add_field(name='****', value='``````')
        #embed.add_field(name='****', value='``````')
        #embed.add_field(name='****', value='``````')
        #embed.add_field(name='****', value='``````')

        await ctx.channel.send(embed=embed)


@bot.command()
async def kanal(ctx):
    
    embed = discord.Embed(title='**KANAL REHBERİ**', description='**Sunucuda bulunan kanalların bulunduğu kategoriye göre bilgi sahibi olmak için rehberi okuyunuz**', color=0xfc0303)

    embed.add_field(name="**AUTONOMOUS**", value="```Proje hakkında genel bilgi almak için inceleyebilirsiniz```")
    embed.add_field(name="**CHAT**", value="```Burada sohbet edebilirsiniz```")
    embed.add_field(name="**PROJECT PROCESS**", value="```Bu bölümde, Projenin dört temel süreci hakkında bilgi edinebilirsiniz```")
    embed.add_field(name="**ACADEMIC PROCESS**", value="```Road MAP süresince karşılaşacağınız sorunları buradan paylaşarak projenin gelişmesine katkı sağlayabilirsiniz```")
    embed.add_field(name="**SUGGESTIONS&QUESTIONS**", value="```Proje, Discord ve BOT hakkındaki sorularınız ve görüşleriniz için burayı kullanabilirsiniz```")
    embed.add_field(name="**VOICE CHANNELS**", value="```Bu bölümde sesli olarak sohbet edebilirsiniz```")
    #embed.add_field(name="****", value="****")


    await ctx.send(embed=embed)



bot.run(TOKEN)
