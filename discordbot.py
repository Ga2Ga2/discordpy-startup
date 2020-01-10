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
async def neko(ctx):
    await ctx.send('にゃーん')


from time import sleep
 
target_time = 10
 
async def cu (secs)(ctx):
    def up_timer(secs):
    for i in range(0,secs):
        print(i)
        sleep(1)
    print("時間です！")
 
 
up_timer(target_time)


async def cd (secs)(ctx):
    def down_timer(secs):
    # for i in range(0,secs):から変更
    for i in range(secs, -1, -1):
        print(i)
        sleep(1)
    print("時間です！")

    
    
bot.run(token)
