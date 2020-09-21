import discord
import random
import variables

client = discord.Client()
prefix = '!chapeu '


@client.event
async def on_ready():
    print('Foi conectado como {0.user}'.format(client))


@client.event
async def on_message(message):
    member = message.author
    grifinoria = discord.utils.get(member.guild.roles, name="Grifinória")
    sonserina = discord.utils.get(member.guild.roles, name="Sonserina")
    corvinal = discord.utils.get(member.guild.roles, name="Corvinal")
    lufalufa = discord.utils.get(member.guild.roles, name="Lufa-Lufa")
    if member == client.user:
        return
    if message.content.startswith(prefix + 'grifinoria'):
        await discord.Member.add_roles(member, grifinoria)
        await message.channel.send('Muito bem, ' + message.author.name + ', Grifinória!')
        await member.remove_roles(sonserina)
        await member.remove_roles(corvinal)
        await member.remove_roles(lufalufa)
    if message.content.startswith(prefix + 'sonserina'):
        await discord.Member.add_roles(member, sonserina)
        await message.channel.send('Muito bem, ' + message.author.name + ', Sonserina!')
        await member.remove_roles(grifinoria)
        await member.remove_roles(corvinal)
        await member.remove_roles(lufalufa)
    if message.content.startswith(prefix + 'corvinal'):
        await discord.Member.add_roles(member, corvinal)
        await message.channel.send('Muito bem, ' + message.author.name + ', Corvinal!')
        await member.remove_roles(grifinoria)
        await member.remove_roles(sonserina)
        await member.remove_roles(lufalufa)
    if message.content.startswith(prefix + 'lufalufa'):
        await discord.Member.add_roles(member, lufalufa)
        await message.channel.send('Muito bem, ' + message.author.name + ', Lufa-Lufa!')
        await member.remove_roles(grifinoria)
        await member.remove_roles(sonserina)
        await member.remove_roles(corvinal)
    if message.content.startswith(prefix + 'sair'):
        await discord.Member.add_roles(member, lufalufa)
        await message.channel.send('Muito bem, ' + message.author.name + ', você limpou seu cargo.')
        await member.remove_roles(grifinoria)
        await member.remove_roles(sonserina)
        await member.remove_roles(corvinal)
        await member.remove_roles(lufalufa)
    if message.content.startswith(prefix + 'random'):
        random.seed()
        await member.remove_roles(grifinoria)
        await member.remove_roles(sonserina)
        await member.remove_roles(corvinal)
        await member.remove_roles(lufalufa)
        casa = random.randint(0, 4)
        if casa == 0:
            await discord.Member.add_roles(member, grifinoria)
            await message.channel.send('Muito bem, ' + message.author.name + ', Grifinória!')
        if casa == 1:
            await discord.Member.add_roles(member, sonserina)
            await message.channel.send('Muito bem, ' + message.author.name + ', Sonserina!')
        if casa == 2:
            await discord.Member.add_roles(member, corvinal)
            await message.channel.send('Muito bem, ' + message.author.name + ', Corvinal!')
        if casa == 3:
            await discord.Member.add_roles(member, lufalufa)
            await message.channel.send('Muito bem, ' + message.author.name + ', Lufa-Lufa!')

client.run(variables.chave)
