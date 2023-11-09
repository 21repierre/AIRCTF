import discord
from discord.ext import commands
import os
import hashlib

FLAG = os.getenv('DISCORD_FLAG')
TOKEN = os.getenv('DISCORD_TOKEN')

if FLAG is None or TOKEN is None:
	exit()

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.command(name="flag", pass_context=True)
async def flag(ctx, *args):
	
	if hasattr(ctx, 'sudo'):
		await ctx.send(f"Bravo, voici le flag: `{FLAG}`.")
	else:
		await ctx.send("Erreur, cette commande est réservé a l'administrateur.")


@bot.command(name="sudo", pass_context=True)
async def sudo(ctx, *args):
	bot_mbr = ctx.message.guild.get_member(bot.user.id)
	if bot_mbr.nick is None:
		await ctx.send("Ce bot n'a pas encore été configuré.")
		return

	if len(args) >= 2:
		passw = args[0]
		h = hashlib.md5()
		h.update((passw + FLAG).encode('utf-8'))
		hPass = h.hexdigest()
		if hPass == bot_mbr.nick:
			cmd = args[1]
			if cmd in sudoable.keys():
				cmd = sudoable[cmd]
				argss = args[2:]
				ctx.sudo = True
				await cmd(ctx, *argss)
		else:
			await ctx.send("Erreur, le mot de passe est incorrect.")
	else:
		await ctx.send("Format: `!sudo <mot_de_passe> <commande> (args)`.")

@bot.command(name="setup", pass_context=True)
async def setup(ctx, *args):
	bot_mbr = ctx.message.guild.get_member(bot.user.id)
	if bot_mbr.nick is not None and not hasattr(ctx, 'sudo'):
		await ctx.send("Ce bot a déja été configuré.")
		return

	if len(args) == 1:
		passw = args[0]
		h = hashlib.md5()
		h.update((passw + FLAG).encode('utf-8'))
		hPass = h.hexdigest()
		await bot_mbr.edit(nick=hPass)
		await ctx.send("Configuration effectuée.")

	else: 
		await ctx.send("Format: `!setup <mot_de_passe>`.")

sudoable = {'flag': flag, 'setup': setup}

bot.run(TOKEN)