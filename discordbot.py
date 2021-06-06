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
    await ctx.send('https://cdn.discordapp.com/attachments/850978385412882445/850987498242572308/05d2870175baf606.jpg')
    await ctx.send('スピードA846 スタミナB691 パワーB+799 根性E+292 賢さC498')
@bot.command()
async def オグリキャップ(ctx):
    await ctx.send('https://cdn.discordapp.com/attachments/850978385412882445/850987498242572308/05d2870175baf606.jpg')

@bot.command()
async def silencesuzuka(ctx):
    await ctx.send('https://cdn.discordapp.com/attachments/850978385412882445/850987501422116874/9e8277cce9ad01c5.jpg')
@bot.command()
async def サイレンススズカ(ctx):
    await ctx.send('https://cdn.discordapp.com/attachments/850978385412882445/850987501422116874/9e8277cce9ad01c5.jpg')    
    
bot.run(token)
