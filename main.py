import discord
import asyncio
import requests
import config

client = discord.Client()

@client.event
async def on_ready():
  async def message(games):
    await client.wait_until_ready()
    while not client.is_closed():
        for game in games:
            await client.change_presence(status = discord.Status.idle, activity = discord.Game(game))
            await asyncio.sleep(10)
  await message(['Discord-Covid-Bot','By CR9'])

@client.event
async def on_message(message):
    if message.content.startswith("!코로나"):
        url = f'https://api.corona-19.kr/korea/?serviceKey={config.apikey}'
        res = requests.get(url)
        covid = res.json()
        TotalCase = format(str(covid["TotalCase"]))
        TotalRecovered = format(str(covid["TotalRecovered"]))
        TotalDeath = format(str(covid["TotalDeath"]))
        updateTime = format(str(covid["updateTime"]))
        embed = discord.Embed(title = f'[ 코로나 ]', description = f'```국내 확진자수 : {TotalCase}\n국내 완치자수 : {TotalRecovered}\n국내 사망자수 : {TotalDeath}```\n기준 : {updateTime}', color=0x3bd1ff)
        await message.channel.send(embed=embed)

client.run(config.token)
