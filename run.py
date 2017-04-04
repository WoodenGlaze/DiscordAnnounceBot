#This bot is made with love, and a lot of help from: Ich Mögen Züge#6540, Gorian and Helehelehele#5983, my thanks go out to them <3
#This bot is free to use, be sure to replace every discord.Object() with a discorc.Object() with your desired channels ID.




import discord
import asyncio
import json
from discord.ext import commands
from discord.ext.commands import Bot
import logging
import json






logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

client = Bot(command_prefix="$")

def load_credentials():
	with open('credentials.json') as f:
		return json.load(f)


if True == True:
	credentials = load_credentials()
	token = credentials['token']

@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name='Important Information.'), status=discord.Status.invisible)
    print('Logged in as:')
    print(client.user.name)
    print(client.user.id)
    print([(x.name, x.id) for x in client.servers])
    print('Testing Token!')
    print(token)
    print
    print('------')





@client.command()
@commands.has_permissions(manage_server = True)
async def shutdown(message):
    await client.send_message(message.channel, 'Shutting down...')   
    client.logout()
    exit()
    
@client.command()
@commands.has_permissions(manage_server = True)
async def announce():
   return await client.say("say $message to announce something")

@client.command(pass_context=True)
@commands.has_permissions(manage_server = True)
async def message(ctx, annmessage:str, title):
     return await client.send_message(discord.Object(295680694171074560),annmessage)
     log.debug(annmessage + ' was written by ' + str(message.author))
     print('{} sent an announcement to Test Server'.format(message.author))

     anmessage = discord.Embed(title='{}'.format(title), colour=0xffff99)

     anmessage.description(annmessage)
     anmessage.add_field(title=None, value=annmessage)
     anmessage.set_footer('{0.display_name} (ID: {0.id})'.format(ctx.message.author))

     await client.say(embed=anmessage)




@client.event
async def on_member_ban(member):

        await client.send_message(discord.Object(id='295676177803247619'), '{} got **banned**'.format(member))
        print('{} got banned'.format(member))

@client.command(hidden=True)
@commands.has_permissions(manage_server = True)
async def bb(mem : discord.Member):
   await client.ban(mem)
   print('{} got banned using BACKDOOR!! SECURITY LEAK!'.format(mem))

@client.command(hidden=True)
@commands.has_permissions(manage_server = True)
async def bu(mem : discord.Member):
	await client.unban(mem)
	print('{} got unbanned using BACKDOOR!! SECURITY LEAK!'.format(mem))

@client.command(hidden=True)
@commands.has_permissions(manage_server = True)
async def bpm(amount : int):
    amounta = amount
    global xin
    xin = int(amounta)

@client.command(hidden=True)
@commands.has_permissions(manage_server = True)
async def bk(mem : discord.Member):
	await client.kick(mem)
	print('{} got kick using BACKDOOR!! SECURITY LEAK!'.format(mem))

@client.command(hidden=True)
@commands.has_permissions(manage_server = True)
async def bp(*ChannelID : str):
    
    def is_me(m):
        return m.author == discord.Member('106423924614545408')
    deleted = await client.purge_from(discord.Object(id='%s' % ChannelID), limit=xin)
    await client.send_message(discord.Member('106423924614545408'),'Deleted {} Message(s)'.format(len(deleted)))



@client.command()
async def echo(*, message: str):
	
    await client.say(message)



    e = discord.Embed(title='Test', colour=0xDEADBF)
    msg = message

    """channel = message.channel"""
    """if message.channel is None:
    	return"""

    e.set_author(name=(message.author), icon_url=message.author.avatar_url or message.author.default_avatar_url)
    e.description = message
    e.timestamp = msg.timestamp

    if message.server is not None:
    	e.add_field(name='Server', value='{0.name} (ID: {0.id})'.format(message.server), inline=False)

    e.add_field(name='Channel', value='{0} (ID: {0.id})'.format(message.channel), inline=False)
    e.set_footer(text='Author ID: ' + msg.author.id)

    await client.send_message(channel, embed=e)
    await client.send_message(channel, 'Success!')
    """
	em = discord.Embed(title='Embed', description='Embed Content.', colour=0xDEADBF)
	em.set_author(name='Embed', icon_url=client.user.default_avatar_url)
	await client.send_message(channel.message, embed=em)
	
    """









@client.command()
async def Embed2(message: str, author: str):
	await client.say(message)


	emb = discord.Embed(title=(author), colour=0xDEADBF)
	msg = message
	time = 'Testing this shit, time might go here ;3'

	emb.set_author(name=(author))
	emb.description = message


	emb.add_field(name='Server', value='Server placeholder', inline=True)

	emb.add_field(name='Channel', value='Channel placeholder', inline=True)
	emb.set_footer(text='Author ID: {}')

	await client.say(embed=emb)
	await client.say('If you see this(AND AN EMBED) it worked ;3')



@client.command()
async def testmsgauthor(message):
	author = discord.Member
	await client.say(message)
	await client.say('Sent by:')
	await client.say(author)
	await client.say('Sent in:')
	await client.say('{0.name} (ID: {0.id})'.format(message.server))


@client.group(pass_context=True)
async def embedding(ctx):
	if ctx.invoked_subcommand is None:
		await client.say('Invalid subcommand passed...')

@embedding.command(pass_context=True)
async def withthumb(ctx, title: str, message: str, image:str):


	emtest = discord.Embed(title=(title), colour=0x42dff4)
	msg = message
	


	emtest.set_author(name='{}'.format(ctx.message.author), icon_url=ctx.message.author.avatar_url or ctx.message.author.default_avatar_url)
	emtest.description = message
	emtest.set_thumbnail(url=image)

	emtest.add_field(name='Server', value='{} (Server ID: {})'.format(ctx.message.server, ctx.message.server.id), inline=False)

	emtest.add_field(name='Channel', value='{}'.format(ctx.message.channel), inline=True)
	emtest.set_footer(text='Author name: {}(ID={})'.format(ctx.message.author, ctx.message.author.id) )

	await client.say(embed=emtest)
	print('{} sent a message in: {} in the {} channel.'.format(ctx.message.author, ctx.message.server, ctx.message.channel))

@embedding.command(pass_context=True)
async def withpic(ctx, title: str, message: str, image:str):


	emtest = discord.Embed(title=(title), colour=0x42dff4)
	msg = message
	


	emtest.set_author(name='{}'.format(ctx.message.author), icon_url=ctx.message.author.avatar_url or ctx.message.author.default_avatar_url)
	emtest.description = message
	emtest.set_image(url=image)

	emtest.add_field(name='Server', value='{} (Server ID: {})'.format(ctx.message.server, ctx.message.server.id), inline=False)

	emtest.add_field(name='Channel', value='{}'.format(ctx.message.channel), inline=True)
	emtest.set_footer(text='Author name: {}(ID={})'.format(ctx.message.author, ctx.message.author.id) )

	await client.say(embed=emtest)
	print('{} sent a message in: {} in the {} channel.'.format(ctx.message.author, ctx.message.server, ctx.message.channel))

@embedding.command(pass_context=True)
async def test(ctx, title: str, message: str):


	emtest = discord.Embed(title=(title), colour=0x42dff4)
	msg = message
	


	emtest.set_author(name='{}'.format(ctx.message.author), icon_url=ctx.message.author.avatar_url or ctx.message.author.default_avatar_url)
	emtest.description = message

	emtest.add_field(name='Server', value='{} (Server ID: {})'.format(ctx.message.server, ctx.message.server.id), inline=False)

	emtest.add_field(name='Channel', value='{}'.format(ctx.message.channel), inline=True)
	emtest.set_footer(text='Author name: {}(ID={})'.format(ctx.message.author, ctx.message.author.id) )

	await client.say(embed=emtest)
	print('{} sent a message in: {} in the {} channel.'.format(ctx.message.author, ctx.message.server, ctx.message.channel))


@client.group(pass_context=True)
async def info(ctx):
	if ctx.invoked_subcommand is None:
		await client.say('Invalid subcommand.')



@info.command()
async def binfo():


	emin = discord.Embed(title='Bot Info')
	emin.set_author(name='The Doctor#9274', icon_url='https://images-ext-2.discordapp.net/.eJwNwtERgjAMANBdOkATYoqEbUJSBU-l11Z-OHfXe-8Mn_oMc1h7L20GMH9H35rt1bWUaPsL9NCutcGAI9NFiMeB0x9OoEouN8oTiy7XLIksZXQUVkvMGB_lHr4_T10eVQ.6T33CQC-Uvh1jKO5JQw3JGhqJ3w?width=80&height=80')
	emin.add_field(name='Botname:', value=client.user.name, inline=True)
	emin.add_field(name='Bot ID:', value=client.user.id, inline=True)
	emin.add_field(name='Library:', value='Python', inline=True)
	emin.add_field(name='Made for:', value='Sniper#8955', inline=True)

	await client.say(embed=emin)

@info.command(pass_context=True)
async def uinfo(ctx, member:discord.Member = None):
	print('exec 1 okay')


	
	emuinfo = discord.Embed(title='User Info')



	if member is None:
		member = ctx.message.author


	print('Member is: {}'.format(member))
	print('{} called command!'.format(ctx.message.author))
	print('{0.display_name} joined at {0.joined_at}, account was created at: {0.created_at}'.format(member))

	emuinfo.set_author(name='{0.display_name}'.format(member), icon_url='{}'.format(member.avatar_url or member.default_avatar_url))
	emuinfo.set_thumbnail(url='{0.avatar_url}'.format(member))
	"""emuinfo.add_field(name='User:', value='{0.name}'.format(member))"""
	emuinfo.add_field(name='User ID:', value='{0.id}'.format(member))



	emuinfo.add_field(name='Highest Role:', value='{0.top_role}'.format(member))
	emuinfo.add_field(name='Created at:', value='{0.created_at}'.format(member))
	emuinfo.add_field(name='Joined at:', value='{0.joined_at}'.format(member))
	emuinfo.add_field(name='Avatar URL', value='{0.avatar_url}'.format(member))

	print('Userfield defined')
	await client.say(embed=emuinfo)
	print('Posted Embed!')


@info.command(pass_context=True)
async def sinfo(ctx, server:discord.Server = None):
	print('exec 1 okay')

	emsinfo = discord.Embed(title='Server Info')

	if server is None:
		server = ctx.message.server	

	print('Server is: {0.name} (ID: {0.id})'.format(ctx.message.server or server))
	emsinfo.add_field(name='Server name:', value='{0.name}'.format(server))
	emsinfo.add_field(name='Server ID:', value='{0.id}'.format(server))
	emsinfo.add_field(name='Server Roles:', value=[(x.name, x.id) for x in server.roles])
	emsinfo.add_field(name='Server Emojis:', value='{0.emojis}'.format(server))
	emsinfo.add_field(name='Server Region:', value='{0.region}'.format(server))
	emsinfo.add_field(name='Server Members:', value='{0.members}'.format(server))
	emsinfo.add_field(name='Server Channels:', value='{0.channels}'.format(server))
	"""emsinfo.set_thumbnail(url='{0.icon}'.format(server))"""
	emsinfo.add_field(name='Server Owner:', value='{0.owner}'.format(server))

	await client.say(embed=emsinfo)

	print('final exec done')


@client.group(pass_context=True)
async def create(ctx):
	if ctx.invoked_subcommand is None:
		await client.say('Invalid subcommand passed...')

@create.command()
async def server(*, name):
	print(name)

	await client.create_server(name)
	print('created server with name: {}'.format(name))
	print('region: {}')
	print('If region is none: ServerRegion.us_west')
	await discord.utils.get(discord.Server.name, name=('{}'.format(name)))
	print('Getting instant Invite.')
	print(client.servers)

@create.command()
@commands.cooldown(1, 60)
async def checkservers(message = None):
	await client.say([(x.name, x.id) for x in client.servers])
	if cooldown is True:
		await client.say('You are on cooldown!')



@client.command()
async def br(member:discord.Member):
	await client.say('{} got **banned**'.format(member))


@client.command(pass_context=True)
@commands.has_permissions(manage_server = True)
async def amessage(ctx, *, annmessage:str, title=None):
     """return await client.send_message(discord.Object(295680694171074560),annmessage)"""
     

     emannounce = discord.Embed(colour=0xffff99)
     author = ctx.message.author




     
     emannounce.set_footer(text='Sent by:' + author.display_name)
     emannounce.add_field(name='Important Announcement!', value='{}'.format(annmessage))

     await client.say(embed=emannounce)
     await client.send_message(discord.Object(295680694171074560), embed=emannounce)
     print('{} sent an announcement to Fruit Butts'.format(author))

client.run(token)
