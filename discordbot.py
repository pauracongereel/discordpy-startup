from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def oguricap(ctx):
    await ctx.send('https://cdn.discordapp.com/attachments/850978385412882445/851012673218281483/oguricap.jpg')
    await ctx.send('スピードA846　スタミナB691　パワーB+799　根性E+292　賢さC498')

@bot.command()
async def silencesuzuka(ctx):
    await ctx.send('https://cdn.discordapp.com/attachments/850978385412882445/851012677001019412/silencesuzuka.jpg')  
    await ctx.send('スピードA+985　スタミナC+509　パワーC+515　根性D329　賢さC414')
    
@bot.command()
async def currenchan(ctx):
    await ctx.send('https://cdn.discordapp.com/attachments/850978385412882445/851012669867425802/currenchan.jpg')  
    await ctx.send('スピードA+963　スタミナC403　パワーB+771　根性D+303　賢さC+555')
    
@bot.command()
async def smartfalcon(ctx):
    await ctx.send('https://cdn.discordapp.com/attachments/850978385412882445/851012680059191336/smartfalcon.jpg')  
    await ctx.send('スピードS+1060　スタミナC+582　パワーB+710　根性D+363　賢さC+542')
    
@bot.command()
async def specialweek(ctx):
    await ctx.send('https://cdn.discordapp.com/attachments/850978385412882445/851012680810758194/specialweek.jpg')  
    await ctx.send('スピードA854　スタミナA861　パワーB623　根性D+389　賢さC+571')
    
@bot.command()
async def symbolirudolf(ctx):
    await ctx.send('https://cdn.discordapp.com/attachments/850978385412882445/851012683867750410/symbolirudolf.jpg')  
    await ctx.send('スピードB+790　スタミナB+790　パワーB+767　根性E+296　賢さC450')
    
@bot.command()
async def taikishuttle(ctx):
    await ctx.send('https://cdn.discordapp.com/attachments/850978385412882445/851479765927329805/taikishuttle.jpg')  
    await ctx.send('スピードS+1093　スタミナD324　パワーB+733　根性E203　賢さC+412')
    
@bot.command()
async def tmoperao(ctx):
    await ctx.send('https://cdn.discordapp.com/attachments/850978385412882445/851479768440635483/tmoperao.jpg')  
    await ctx.send('スピードS+1012　スタミナC+591　パワーC+550　根性D307　賢さB607')
    
@bot.command()
async def tokaiteio(ctx):
    await ctx.send('https://cdn.discordapp.com/attachments/850978385412882445/851479764477018152/tokaiteio.jpg')  
    await ctx.send('スピードB697　スタミナB673　パワーB667　根性C413　賢さC+513')
bot.run(token)
