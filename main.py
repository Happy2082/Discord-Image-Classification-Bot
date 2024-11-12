import discord
from discord.ext import commands
from testy import ImageAI

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Zalogowaliśmy się jako {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Cześć! Jestem botem, {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def image(ctx):
    print(ctx.message.attachments)
    if len(ctx.message.attachments) >= 1:
        for attachment in ctx.message.attachments:
            await attachment.save(f'./Images/{attachment.filename}')
            user_image = f'./Images/{attachment.filename}'
            message = ImageAI(user_image)
            result1 = len(message)
            await ctx.send(message)
    else:
        await ctx.send(f'There was no image attached.')


        
bot.run("")