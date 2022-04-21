import discord
import json
from discord import Embed
from discord.ext import commands
import colorama
import json
from colorama import Fore, Back, Style
import sys, time
with open('./config.json', 'r') as cjson:
    config = json.load(cjson)
colorama.init()
bot = commands.Bot(command_prefix = config["prefix"], description = "Bot de Nathoune")

print('\033[36m' + '                     ██▓    ▓█████      ▄▄▄▄    ▒█████  ▄▄▄█████▓\n                    ▓██▒    ▓█   ▀     ▓█████▄ ▒██▒  ██▒▓  ██▒ ▓▒\n                    ▒██░    ▒███       ▒██▒ ▄██▒██░  ██▒▒ ▓██░ ▒░\n                    ▒██░    ▒▓█  ▄     ▒██░█▀  ▒██   ██░░ ▓██▓ ░ \n                    ░██████▒░▒████    ▒░▓█  ▀█▓░ ████▓▒░  ▒██▒ ░ \n                    ░ ▒░▓  ░░░ ▒░     ░░▒▓███▀▒░ ▒░▒░▒░    ▒ ░░   \n                    ░ ░ ▒  ░ ░ ░      ░▒░▒   ░   ░ ▒ ▒░     ░    \n                      ░ ░      ░        ░    ░ ░ ░ ░ ▒    ░      \n                        ░  ░   ░      ░ ░          ░ ░          ')
print('\033[39m')

message = "Mise en ligne, veuiller patientez un instant...\n\n"
message2 = "Tempts estimé : "
message3 = "5 secondes restantes"
message4 = " . . . ."

for char in message:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.03)

for char in message2:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.0005)

for char in message3:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.05)
    
for char in message4:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.15)

@bot.event
async def on_ready():
    activity = discord.Game(name="être inutile", type=1)
    await bot.change_presence(status=discord.Status.online, activity=activity)
    print('\033[32m' + '\n\n                >En ligne< \n\n' + '\033' + '\n\n>>> NE SURTOUT PAS FERMER CETTE FENÊTRE ! LE BOT EST EN LIGNE UNIQUEMENT QUAND CETTE DERNIÈRE EST OUVERTE ! <<<' + '\033[39m' + '\n\n\n®Nathoune 2021')

@bot.event
async def on_message(message):
    if message.content.lower() == ('salut'):
        channel = message.channel
        await channel.send('Yo ! Comment tu vas ?')

    if message.content.lower() == ('yo'):
        channel = message.channel
        await channel.send('Salut !')

    if message.content.lower() == ('comment tu vas ?'):
        channel = message.channel
        await channel.send('Moi très bien ! Après les autres je sais pas...')

    if message.content.lower() == ('bonjour'):
        channel = message.channel
        await channel.send('Bonsoir ! Je suis vraiment le pire bot... Désolé...')

    if message.content.lower() == ('aide moi'):
        channel = message.channel
        await channel.send('Je suis pas dispo mdr')

    if message.content.lower() == ('aide-moi'):
        channel = message.channel
        await channel.send('Je suis pas dispo mdr')

    if message.content.lower() == ('bravo'):
        channel = message.channel
        await channel.send('Bravoooooooo ! Tu es trop fort ! (je sais pas ce que tu as fait mais bravo)')

    if message.content.lower() == ('pourquoi'):
        channel = message.channel
        await channel.send('Je sais pas demande lui...')

    if message.content.lower() == ('pourquoi ?'):
        channel = message.channel
        await channel.send('Je sais pas demande lui...')

    if message.content.lower() == ('pk'):
        channel = message.channel
        await channel.send('Je sais pas demande lui...')

    if message.content.lower() == ('pk ?'):
        channel = message.channel
        await channel.send('Je sais pas demande lui...')

    if message.content.lower() == ('mdr'):
        channel = message.channel
        await channel.send('Trop drôle mdrrr')

    if message.content.lower() == ('ptdr'):
        channel = message.channel
        await channel.send('Jsuis plié de rire mdr')

    if message.content.lower() == ('le bot'):
        channel = message.channel
        await channel.send('Qui ? Moi ? Je suis mieux que vos bots anti raids... Moi je créer des raids mdr (c faux je suis éclaté)')

    if message.content.lower() == ('bot'):
        channel = message.channel
        await channel.send('Qui ? Moi ? Je suis mieux que vos bots anti raids... Moi je créer des raids mdr (c faux je suis éclaté)')

    if message.content.lower() == ('le bot est éclaté'):
        channel = message.channel
        await channel.send('Oui')

    if message.content.lower() == ('il est éclaté'):
        channel = message.channel
        await channel.send('Oui, totalement')

    if message.content.lower() == ('le bot est nul'):
        channel = message.channel
        await channel.send('Oui je sers à rien')

    if message.content.lower() == ('tu sers à rien'):
        channel = message.channel
        await channel.send('Oui')

    if message.content.lower() == ('tu sers à rien @Le Bot'):
        channel = message.channel
        await channel.send('Oui')

    if message.content.lower() == ('re'):
        channel = message.channel
        await channel.send('Re.. ça va depuis ?')

    if message.content.lower() == ('nathoune'):
        channel = message.channel
        await channel.send('Mon créateur mdr')

    if message.content.lower() == ('bien et toi ?'):
        channel = message.channel
        await channel.send('Perso ça va bien merci')

    if message.content.lower() == ('bien et toi'):
        channel = message.channel
        await channel.send('Perso ça va bien merci')

    if message.content.lower() == ('raid'):
        channel = message.channel
        await channel.send('Qui veut raid ici je vais le démarer')
        
    if message.content.lower() == ('tg le bot'):
        channel = message.channel
        await channel.send('Depuis quand je me prends des tg comme ça moi')
        
    if message.content.lower() == ('tg'):
        channel = message.channel
        await channel.send('Ouais tg (sauf si on parle à moi mdrr)')
        
    if message.content.lower() == ('ta gueule'):
        channel = message.channel
        await channel.send('Ouais tg (sauf si on parle à moi mdrr)')
        
    if message.content.lower() == ('ta gueule le bot'):
        channel = message.channel
        await channel.send('Depuis quand je me prends des ta gueule comme ça moi')
    
    if message.content.lower() == ('putain'):
        channel = message.channel
        await channel.send('__**PARDON ? QU ENTENGE ? UNE INJURE ? JE VAIS TE KICK DU SERV MOI !**__ mdr tkt je suis un peu inutile sur ce serv')
    
    if message.content.lower() == ('merde'):
        channel = message.channel
        await channel.send('__**PARDON ? QU ENTENGE ? UNE INJURE ? JE VAIS TE KICK DU SERV MOI !**__ mdr tkt je suis un peu inutile sur ce serv')

    if message.content.lower() == ('jsp'):
        channel = message.channel
        await channel.send('Moi non plus lol')

    if message.content.lower() == ('je sais pas'):
        channel = message.channel
        await channel.send('Moi non plus lol')
        
    if message.content.lower() == ('lol'):
        channel = message.channel
        await channel.send('lLlooOooOoOOlLll :joy::joy::joy:')

    if message.content.lower() == ('discord'):
        channel = message.channel
        await channel.send('Nous sommes sur cette application ! (truc de ouf comment j`informe les gens, dingue)')

    if message.content.lower() == ('ban'):
        channel = message.channel
        await channel.send('Qui va ban qui ? Je suis le maître des lieux (faux je sers à rien)')

    if message.content.lower() == ('bannir'):
        channel = message.channel
        await channel.send('Qui va ban qui ? Je suis le maître des lieux (faux je sers à rien)')

    if message.content.lower() == ('python'):
        channel = message.channel
        await channel.send('Mon language de programmation !')

    if message.content.lower() == ('java'):
        channel = message.channel
        await channel.send('Mouais :yawning_face:')

    if message.content.lower() == ('abonnement'):
        channel = message.channel
        await channel.send('Go > https://www.youtube.com/Nathoune/c/?sub_confirmation=1')

    if message.content.lower() == ('hello'):
        channel = message.channel
        await channel.send('Hello everyone, welcome to a brand new tutorial, today we create a script with python (prends l`accent indien)')

    if message.content.lower() == ('vfx'):
        channel = message.channel
        await channel.send('Que ce monde est passionnant !')

    if message.content.lower() == ('3d'):
        channel = message.channel
        await channel.send('Que ce monde est passionnant !')

    if message.content.lower() == ('youtube'):
        channel = message.channel
        await channel.send('YouTube est un site web d’hébergement de vidéos et un média social sur lequel les utilisateurs peuvent envoyer, regarder, commenter, évaluer et partager des vidéos en streaming. Wikip.. non moi même mdr (crois moi stp)')
        
    if message.content.lower() == ("{}h".format(config["prefix"])):
        channel = message.channel
        embed1 = Embed(title="Commandes et mots :", color=0xffab33)
        embed1.add_field(name="{}h".format(config["prefix"]), value="Envoyer ce message", inline=False)
        embed1.add_field(name="{}news".format(config["prefix"]), value="Afficher les nouveautés !", inline=True)
        embed1.add_field(name="Salut", value="Réponse de Le_Bot", inline=False)
        embed1.add_field(name="Yo", value="Réponse de Le_Bot", inline=False)
        embed1.add_field(name="Comment tu vas ?", value="Réponse de Le_Bot", inline=False)
        embed1.add_field(name="Bonjour", value="Réponse de Le_Bot", inline=False)
        embed1.add_field(name="Aide moi", value="Réponse de Le_Bot", inline=False)
        embed1.add_field(name="Aide-moi", value="Réponse de Le_Bot", inline=False)
        embed1.add_field(name="Bravo", value="Réponse de Le_Bot", inline=False)
        embed1.add_field(name="Pourquoi ?", value="Réponse de Le_Bot", inline=False)
        embed1.add_field(name="Pourquoi ?", value="Réponse de Le_Bot", inline=False)
        embed1.add_field(name="Pk", value="Réponse de Le_Bot", inline=False)
        embed1.add_field(name="Pk ?", value="Réponse de Le_Bot", inline=False)
        embed1.add_field(name="Mdr", value="Réponse de Le_Bot", inline=False)
        embed1.add_field(name="Ptdr", value="Réponse de Le_Bot", inline=False)
        embed1.add_field(name="Bot", value="Réponse de Le_Bot", inline=False)
        embed1.add_field(name="Le bot", value="Réponse de Le_Bot", inline=False)
        embed1.add_field(name="Le bot est éclaté", value="Réponse de Le_Bot", inline=False)
        embed1.add_field(name="Le bot est nul", value="Réponse de Le_Bot", inline=False)
        embed1.add_field(name="Tu sers à rien", value="Réponse de Le_Bot", inline=False)
        embed1.add_field(name="Re", value="Réponse de Le_Bot", inline=False)
        embed1.add_field(name="Nthoune", value="Réponse de Le_Bot", inline=False)
        embed1.add_field(name="Bien et toi ?", value="Réponse de Le_Bot", inline=False)
        embed1.add_field(name="Bien et toi", value="Réponse de Le_Bot", inline=False)
        embed1.add_field(name="Raid", value="Réponse de Le_Bot", inline=False)
        embed1.add_field(name="Tg le bot", value="Réponse de Le_Bot", inline=False)
        embed1.add_field(name="Tg", value="Réponse de Le_Bot", inline=False)
        embed1.add_field(name="Ta gueule", value="Réponse de Le_Bot", inline=False)
        embed1.add_field(name="Ta gueule le bot", value="Réponse de Le_Bot", inline=False)
        embed1.add_field(name="Putain", value="Réponse de Le_Bot", inline=False)
        embed1.add_field(name="Merde", value="Réponse de Le_Bot", inline=False)
        embed1.add_field(name="Jsp", value="Réponse de Le_Bot", inline=False)
        embed1.add_field(name="Je sais pas", value="Réponse de Le_Bot", inline=False)
        embed1.add_field(name="Lol", value="Réponse de Le_Bot", inline=False)
        embed1.set_image(url="https://cdn-0.emojis.wiki/emoji-pics/facebook/ok-hand-facebook.png")     
        await message.channel.send(embed=embed1)
        
    if message.content.lower() == ("{}news".format(config["prefix"])):
        channel = message.channel
        embed1 = Embed(title="Voici le nouveautés !", color=0xffab33)
        embed1.add_field(name="Discord", value="Réponse de Le_Bot", inline=False)
        embed1.add_field(name="Ban", value="Réponse de Le_Bot", inline=False)
        embed1.add_field(name="Bannir", value="Réponse de Le_Bot", inline=False)
        embed1.add_field(name="Python", value="Réponse de Le_Bot", inline=False)
        embed1.add_field(name="Java", value="Réponse de Le_Bot", inline=False)
        embed1.add_field(name="Abonnement", value="Réponse de Le_Bot", inline=False)
        embed1.add_field(name="Hello", value="Réponse de Le_Bot", inline=False)
        embed1.add_field(name="Vfx", value="Réponse de Le_Bot", inline=False)
        embed1.add_field(name="3D", value="Réponse de Le_Bot", inline=False)
        embed1.add_field(name="YouTube", value="Réponse de Le_Bot", inline=False)
        embed1.set_image(url="https://cdn-0.emojis.wiki/emoji-pics/facebook/ok-hand-facebook.png")     
        await message.channel.send(embed=embed1)

    
bot.run(config["token"])
