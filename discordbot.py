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
    await ctx.send('https://cdn.discordapp.com/attachments/850978385412882445/850978472674459668/aac4265003b57811.jpg')


@bot.command()
async def silencesuzuka(ctx):
    await ctx.send('https://cdn.discordapp.com/attachments/850978385412882445/850986927414837308/b2cdaa4578310381.jpg')
    
    
bot.run(token)
