from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = NjY1MDExNTg3MTk0NjgzNDEy.XhfdGw.SVHjZZsZA4c5oq1brqQjsaFPI0s


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)
        
    
@bot.command()
async def '/neko'(ctx):
    await ctx.send('にゃーん')


bot.run(token)
