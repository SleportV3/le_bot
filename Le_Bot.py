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


list = [
    {
        'name': 'yo',
        'value': 'Salut !'
    },
    {
        'name': 'comment tu vas ?',
        'value': 'Moi très bien ! Après les autres je sais pas...'
    },
    {
        'name': 'bonjour',
        'value': 'Bonsoir ! Je suis vraiment le pire bot... Désolé...'
    },
    {
        'name': 'salut',
        'value': 'Yo ! Comment tu vas ?'
    },
    {
        'name': 'aide moi',
        'value': 'Je suis pas dispo mdr',
    },
    {
        'name': 'aide-moi',
        'value': 'Je suis pas dispo mdr',
    },
    {
        'name': 'bravo',
        'value': 'Bravoooooooo ! Tu es trop fort ! (je sais pas ce que tu as fait mais bravo)'
    },
    {
        'name': 'pourquoi',
        'value': 'Je sais pas demande lui...',
    },
    {
        'name': 'pourquoi ?',
        'value': 'Je sais pas demande lui...',
    },
    {
        'name': 'pk',
        'value': 'Je sais pas demande lui...',
    },
    {
        'name': 'pk ?',
        'value': 'Je sais pas demande lui...',
    },
    {
        'name': 'mdr',
        'value': 'Trop drôle mdrrr'
    },
    {
        'name': 'ptdr',
        'value': 'Jsuis plié de rire mdr'
    },
    {
        'name': 'le bot',
        'value': 'Qui ? Moi ? Je suis mieux que vos bots anti raids... Moi je créer des raids mdr (c faux je suis éclaté)'
    },
    {
        'name': 'bot',
        'value': 'Qui ? Moi ? Je suis mieux que vos bots anti raids... Moi je créer des raids mdr (c faux je suis éclaté)'
    },
    {
        'name': 'le bot est éclaté',
        'value': 'Oui'
    },
    {
        'name': 'il est éclaté',
        'value': 'Oui, totalement'
    },
    {
        'name': 'le bot est nul',
        'value': 'Oui je sers à rien'
    },
    {
        'name': 'tu sers à rien',
        'value': 'Oui'
    },
    {
        'name': 're',
        'value': 'Re.. ça va depuis ?'
    },
    {
        'name': 'nathoune',
        'value': 'Mon créateur mdr'
    },
    {
        'name': 'bien et toi ?',
        'value': 'Perso ça va bien merci'
    },
    {
        'name': 'raid',
        'value': 'Qui veut raid ici je vais le démarer'
    },
    {
        'name': 'tg le bot',
        'value': 'Depuis quand je me prends des tg comme ça moi'
    },
    {
        'name': 'tg',
        'value': 'Ouais tg (sauf si on parle à moi mdrr)'
    },
    {
        'name': 'ta gueule',
        'value': 'Ouais tg (sauf si on parle à moi mdrr)'
    },
    {
        'name': 'ta gueule le bot',
        'value': 'Depuis quand je me prends des ta gueule comme ça moi'
    },
    {
        'name': 'putain',
        'value': '__**PARDON ? QU ENTENGE ? UNE INJURE ? JE VAIS TE KICK DU SERV MOI !**__ mdr tkt je suis un peu inutile sur ce serv'
    },
    {
        'name': 'merde',
        'value': '__**PARDON ? QU ENTENGE ? UNE INJURE ? JE VAIS TE KICK DU SERV MOI !**__ mdr tkt je suis un peu inutile sur ce serv'
    },
    {
        'name': 'jsp',
        'value': 'Moi non plus lol'
    },
    {
        'name': 'je sais pas',
        'value': 'Moi non plus lol'
    },
    {
        'name': 'lol',
        'value': 'lLlooOooOoOOlLll :joy::joy::joy:'
    },
    {
        'name': 'discord',
        'value': 'Nous sommes sur cette application ! (truc de ouf comment j`informe les gens, dingue)',
    },
    {
        'name': 'ban',
        'value': 'Qui va ban qui ? Je suis le maître des lieux (faux je sers à rien)'
    },
    {
        'name': 'bannir',
        'value': 'Qui va ban qui ? Je suis le maître des lieux (faux je sers à rien)'
    },
    {
        'name': 'python',
        'value': 'Mon language de programmation !',
    },
    {
        'name': 'java',
        'value': 'Mouais :yawning_face:'
    },
    {
        'name': 'abonnement',
        'value': 'Go > https://www.youtube.com/Nathoune/c/?sub_confirmation=1'
    },
    {
        'name': 'hello',
        'value': 'Hello everyone, welcome to a brand new tutorial, today we create a script with python (prends l`accent indien)'
    },
    {
        'name': 'vfx',
        'value': 'Que ce monde est passionnant !'
    },
    {
        'name': '3d',
        'value': 'Que ce monde est passionnant !'
    },
    {
        'name': 'youtube',
        'value': 'YouTube est un site web d’hébergement de vidéos et un média social sur lequel les utilisateurs peuvent envoyer, regarder, commenter, évaluer et partager des vidéos en streaming. Wikip.. non moi même mdr (crois moi stp)'
    }


]


@bot.event
async def on_message(message):

    

    for obj in list:
        if message.content.lower() == obj['name']:
            channel = message.channel
            await channel.send(obj['value'])


        
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
