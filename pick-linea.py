import discord
import random
import os
from discord.ext import commands


TOKEN = os.getenv('TOKEN')

intents = discord.Intents.default()
intents.members = True
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

top_laners = ["Aatrox", "Akali", "Briar", "Camille", "Cho'Gath", "Darius", "Dr. Mundo", "Fiora", "Gangplank", "Garen", "Gnar", "Gwen", "Illaoi", "Irelia", "Jax", "Jayce", "Kayle", "Kennen", "Kled", "K'Sante", "Malphite", "Mordekaiser", "Nasus", "Olaf", "Ornn", "Pantheon", "Poppy", "Quinn", "Renekton", "Riven", "Rumble", "Sett", "Shen", "Singed", "Sion", "Tahm Kench", "Teemo", "Trundle", "Tryndamere", "Urgot", "Volibear", "Yone", "Yorick"]

junglers = ["Amumu", "Bel'Veth", "Brand", "Briar", "Diana", "Ekko", "Elise", "Evelynn", "Fiddlesticks", "Gragas", "Graves", "Hecarim", "Ivern", "Jarvan IV", "Jax", "Karthus", "Kayn", "Kha'Zix", "Kindred", "Lee Sin", "Lillia", "Maokai", "Master Yi", "Nidalee", "Nocturne", "Nunu & Willump", "Pantheon", "Poppy", "Rammus", "Rek'Sai", "Rengar", "Sejuani", "Shaco", "Shyvana", "Skarner", "Taliyah", "Talon", "Trundle", "Udyr", "Vi", "Viego", "Volibear", "Warwick", "Wukong", "Xin Zhao", "Zac"]

mid_laners = ["Ahri", "Akali", "Akshan", "Anivia", "Annie", "Aurelion Sol", "Azir", "Cassiopeia", "Corki", "Diana", "Ekko", "Fizz", "Galio", "Gragas", "Heimerdinger", "Irelia", "Kassadin", "Katarina", "LeBlanc", "Lissandra", "Lux", "Malzahar", "Neeko", "Orianna", "Pantheon", "Qiyana", "Ryze", "Seraphine", "Swain", "Sylas", "Syndra", "Taliyah", "Talon", "Twisted Fate", "Veigar", "Vel'Koz", "Vex", "Viktor", "Vladimir", "Xerath", "Yasuo", "Yone", "Zed", "Ziggs", "Zoe"]

adcs = ["Aphelios", "Ashe", "Caitlyn", "Draven", "Ezreal", "Jhin", "Jinx", "Kai'Sa", "Kalista", "Kog'Maw", "Lucian", "Miss Fortune", "Samira", "Senna", "Sivir", "Tristana", "Twitch", "Varus", "Vayne", "Xayah", "Zeri"]

supports = ["Alistar", "Bard", "Blitzcrank", "Brand", "Braum", "Janna", "Karma", "Leona", "Lulu", "Lux", "Morgana", "Nami", "Nautilus", "Pyke", "Rakan", "Renata Glasc", "Rell", "Senna", "Seraphine", "Sona", "Soraka", "Swain", "Tahm Kench", "Taric", "Thresh", "Yuumi", "Zilean", "Zyra"]

def campeon(linea):
    if linea == "Top":
        return random.choice(top_laners)
    elif linea == "Jungla":
        return random.choice(junglers)
    elif linea == "Mid":
        return random.choice(mid_laners)
    elif linea == "ADC":
        return random.choice(adcs)
    elif linea == "Supp":
        return random.choice(supports)

@bot.event
async def on_ready():
    print(f'Bot conectado como {bot.user}')

@bot.command(name='lol')
async def linea(ctx, *players):
    lineas = ["Top", "Jungla", "Mid", "ADC", "Supp"]
    random.shuffle(lineas)

    response = ""
    for i, player in enumerate(players):
        linea = lineas[i]
        champ = campeon(linea)
        response += f"{player} jugará {linea} con {champ}\n"

    await ctx.send(response)

bot.run(TOKEN)
