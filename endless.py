import discord
from discord.ext.commands import bot
from discord.ext import commands
import asyncio

Client = discord.Client()
bot = commands.Bot(command_prefix = ".")
wallsOn = False
wallsTime = 5
count = 0
        
@bot.event
async def on_ready():
    activity = discord.Game(name=".usage for help")#Changes 'playing' to this
    await bot.change_presence(game = activity)
    print("Logged in as " + bot.user.name)#Trivial log message for startup
    print("ID: " + bot.user.id)#Prints the id of the bot

async def wallchecking():
    await bot.wait_until_ready()#Waits until the bot is ready to take commands
    global wallsOn#Calls the global variables
    global wallsTime
    global count
    channel = discord.Object(id="462161429919694850")#Gets the walls channel id
    message = "<@&459344067369631774> check walls!"#Mentions the 'Endless' role
    while wallsOn == False:#While walls are off
        await asyncio.sleep(1)#Checks every second
        if wallsOn == True:#Checks whether walls are on or not
            while wallsOn == True:#If they are on
                await asyncio.sleep(60)#Will be 60
                count = (count+1)#Increases once per minute//resets if .check is done
                if count >= wallsTime:#If count is equal to or greater than the time for wall checking
                    await bot.send_message(channel, message)
                    await asyncio.sleep(60)#Message will then be sent after that every 2 minutes

@bot.command(pass_context=True)
async def check(ctx):
    global count#Calls the global variable
    if "459344067369631774" in [role.id for role in ctx.message.author.roles]:#Must have endless role
        if wallsOn == True:#Checks wall checking is turned on
            count = 0#Count is reset to 0
            await bot.say(ctx.message.author.mention+" has checked walls!")#Confirmation message
        else:#If wall checking is turned off
            await bot.say("Wall checking is not currently turned on.")
    else:#Lack of permission
        await bot.say("You do not have permission to use this command.")

@bot.command(pass_context=True)
async def weewoo(ctx, side:str = None):
    if "459344067369631774" in [role.id for role in ctx.message.author.roles]:#Must have endless role
        channel = discord.Object(id="462161429919694850")
        if side is None:
            await bot.say("You need to specify a side that we are being raided from!")
        elif side == "north":
            message = "@everyone we are being raided on the North side!!!"
            await bot.send_message(channel, message)
            await bot.send_message(channel, message)
            await bot.send_message(channel, message)
            await bot.send_message(channel, message)
            await bot.send_message(channel, message)
        elif side == "south":
            message = "@everyone we are being raided on the South side!!!"
            await bot.send_message(channel, message)
            await bot.send_message(channel, message)
            await bot.send_message(channel, message)
            await bot.send_message(channel, message)
            await bot.send_message(channel, message)
        elif side == "east":
            message = "@everyone we are being raided on the East side!!!"
            await bot.send_message(channel, message)
            await bot.send_message(channel, message)
            await bot.send_message(channel, message)
            await bot.send_message(channel, message)
            await bot.send_message(channel, message)
        elif side == "west":
            message = "@everyone we are being raided on the West side!!!"
            await bot.send_message(channel, message)
            await bot.send_message(channel, message)
            await bot.send_message(channel, message)
            await bot.send_message(channel, message)
            await bot.send_message(channel, message)
        else:
            await bot.say(".weewoo (side)")           
    else:
        await bot.say("You do not have permission to use this command.")
    
                    

@bot.event
async def on_member_join(member):#When a member joins
    channel = member.server.get_channel("459806304769146890")#Gets the welcome-goodbye channel ID
    msg = "Welcome to the Official Endless Discord server, {0.mention} :thumbsup:" #Message that is put in the channel
    await bot.send_message(channel, msg.format(member)) #Formatted to add the user that has joined

@bot.event
async def on_member_remove(member):#When a member leaves
    channel = member.server.get_channel("459806304769146890")#Gets the welcome-goodbye channel ID
    msg = "Goodbye {0.mention}, thanks for coming :thumbsdown:"#Message that is put in the channel
    await bot.send_message(channel, msg.format(member))#Formatted to add the user that left

@bot.command(pass_context=True)
async def setwalltime(ctx, time:int = None):#Sets the time to check walls
    if "459287625187065856" in [role.id for role in ctx.message.author.roles]:#Must be leader
        global wallsTime
        global count
        if time is None:#No time given
            wallsTime = (5)#Resets the wall check time to default 5 minutes
            await bot.say("Wall time has been reset to 5 minutes.")
            count = 0
        else:
            wallsTime = time#Sets a new time
            await bot.say("A new wall time has been set.")
            count = 0
    else:#Lack of permission
        await bot.say("You do not have permission to use this command.")
        
    
    
        

@bot.command(pass_context=True)
async def togglewalls(ctx):#Turns wall checking on or off
    if "459287625187065856" in [role.id for role in ctx.message.author.roles]:#Must be leader
        global wallsOn
        global count
        if wallsOn == True:#If wall checking is on
            wallsOn = False#Wall checking is turned off
            await bot.say("Wall checking has been turned off.")
            count = 0#Resets the count for wall checking
        else:
            wallsOn = True#Turns wall checking on
            await bot.say("Wall checking has been turned on.")
    else:#Lack of permission
        await bot.say("You do not have permission to use this command.")
   
@bot.command(pass_context=True)
async def test(ctx):#Check for online bot
    await bot.say("Testing...")

@bot.command(pass_context=True)
async def clear(ctx,number:int = None):#Clear a certain number of messages
    if number is None:#Number of messages is not given
        await bot.say("You need to specify the number of messages to delete.")
        #Must have the correct role to do this
    elif "459287625187065856" in [role.id for role in ctx.message.author.roles] or "459287454172839936" in [role.id for role in ctx.message.author.roles] or "459287110810075156" in [role.id for role in ctx.message.author.roles]:       
        messages = []#Creates a list for the messages to be put into
        number = (number + 1)#Deletes the command aswell as the specified number of messages
        async for x in bot.logs_from(ctx.message.channel, limit = number):
            messages.append(x)#Adds all the messages to the list
        await bot.delete_messages(messages)#Deletes the list
    else:#Lack of permissions
        await bot.say("You do not have permission to use this command.")

@bot.command(pass_context=True)
async def say(ctx,message = None):#As if the bot is speaking
    #Must have the correct role to do this
    if "459287625187065856" in [role.id for role in ctx.message.author.roles] or "459287454172839936" in [role.id for role in ctx.message.author.roles] or "459287110810075156" in [role.id for role in ctx.message.author.roles]:
        if message is None:#No message is given
            await bot.say("You need to specify what you want me to say.")
        else:
            await bot.delete_message(ctx.message)#Deletes the user message
            await bot.say(message)#Bot says the message
    else:#Lack of permissions
        await bot.say("You do not have permission to use this command.")

@bot.command(pass_context=True)
async def kick(ctx, member: discord.User = None, *, reason:str = None):#Kicks a user
    if "459287625187065856" in [role.id for role in ctx.message.author.roles] or "459287454172839936" in [role.id for role in ctx.message.author.roles] or "459287110810075156" in [role.id for role in ctx.message.author.roles] or "459286909018046470" in [role.id for role in ctx.message.author.roles]:
        if member is None:#No user given
            await bot.say("You need to specify a user to kick.")
        elif reason is None:#No reason given
            await bot.say("You need to give a reason.")
        elif member.id == "459426194367053872":#If trying to kick the bot.
            await bot.say("You cannot kick me.")
        elif member.id == "165572447725289472":#If trying to kick Jamie
            await bot.say("You cannot kick Jamie.")
        elif member.id == ctx.message.author.id:#If trying to kick themselves
            await bot.say("You cannot kick yourself.")
        elif "459287625187065856" in [role.id for role in member.roles]:#Cannot kick a leader
            await bot.say("You cannot kick a Leader.")
        elif "459287454172839936" in [role.id for role in member.roles]:#Cannot kick a manager
            await bot.say("You cannot kick a Manager.")
        elif "459287110810075156" in [role.id for role in member.roles]:#Cannot kick a co-leader
            await bot.say("You cannot kick a Co-Leader.")
        elif "459286909018046470" in [role.id for role in member.roles]:#Cannot kick a mod+
            await bot.say("You cannot kick a Mod +.")   
        else:
            #Must have correct role to use this
            await bot.send_message(member, "You have been kicked from the discord for: "+reason)
            await bot.kick(member)#Kicks the member
            await bot.say("That person has been kicked from this discord.")
            await bot.send_message(discord.Object(id="459797212965109816"),"**Kick**")#Logs the kick in the 'log' channel
            await bot.send_message(discord.Object(id="459797212965109816"),ctx.message.author.name)
            await bot.send_message(discord.Object(id="459797212965109816"),member)
            await bot.send_message(discord.Object(id="459797212965109816"),reason)
            await bot.send_message(discord.Object(id="459797212965109816"),"=======================")
    else:#Lack of permission
        await bot.say("You do not have permission to use this command.")

@bot.command(pass_context=True)
async def ban(ctx, member: discord.User = None, *, reason:str = None):#Bans a user
    if "459287625187065856" in [role.id for role in ctx.message.author.roles] or "459287454172839936" in [role.id for role in ctx.message.author.roles] or "459287110810075156" in [role.id for role in ctx.message.author.roles]:
        if member is None:#No user given
            await bot.say("You need to specify a user to ban.")
        elif reason is None:#No reason given
            await bot.say("You need to give a reason.")
        elif member.id == "459426194367053872":#If trying to ban the bot.
            await bot.say("You cannot ban me.")
        elif member.id == "165572447725289472":#If trying to ban Jamie
            await bot.say("You cannot ban Jamie.")
        elif member.id == ctx.message.author.id:#If trying to ban themselves
            await bot.say("You cannot ban yourself.")
        elif "459287625187065856" in [role.id for role in member.roles]:#Cannot ban a leader
            await bot.say("You cannot ban a Leader.")
        elif "459287454172839936" in [role.id for role in member.roles]:#Cannot ban a manager
            await bot.say("You cannot ban a Manager.")
        elif "459287110810075156" in [role.id for role in member.roles]:#Cannot ban a co-leader
            await bot.say("You cannot ban a Co-Leader.")
        else:
            #Must have correct role to use this
            await bot.ban(member)#Bans the member
            await bot.say("That person has been banned from this discord.")
            await bot.send_message(discord.Object(id="459797212965109816"),"**Ban**")#Logs the ban in the 'log' channel
            await bot.send_message(discord.Object(id="459797212965109816"),ctx.message.author.name)
            await bot.send_message(discord.Object(id="459797212965109816"),member)
            await bot.send_message(discord.Object(id="459797212965109816"),reason)
            await bot.send_message(discord.Object(id="459797212965109816"),"=======================")
    else:#Lack of permission
        await bot.say("You do not have permission to use this command.")

@bot.command(pass_context=True)
async def warn(ctx, member:discord.User = None, *, reason:str = None):#Warns a user
    if "459287625187065856" in [role.id for role in ctx.message.author.roles] or "459287454172839936" in [role.id for role in ctx.message.author.roles]:#Must be leader
        if member is None:#No member given
            await bot.say("You need to specify a user to warn.")
        elif reason is None:#No reason given
            await bot.say("You need to give a reason.")
        elif member.id == "459426194367053872":#Trying to warn the bot
            await bot.say("You cannot warn me.")
        elif member.id == "165572447725289472":#Trying to warn Jamie
            await bot.say("You cannot warn Jamie.")
        elif member.id == ctx.message.author.id:#Trying to warn themselves
            await bot.say("You cannot warn yourself.")
        else:
            await bot.say("That person has been warned.")
            await bot.send_message(discord.Object(id="459797212965109816"),"**Warn**")#Logs the warn in the 'log' channel
            await bot.send_message(discord.Object(id="459797212965109816"),ctx.message.author.name)
            await bot.send_message(discord.Object(id="459797212965109816"),member)
            await bot.send_message(discord.Object(id="459797212965109816"),reason)
            await bot.send_message(discord.Object(id="459797212965109816"),"=======================")
    else:#Lack of permission
        await bot.say("You do not have permission to use this command.")

@bot.command(pass_context=True)
async def promote(ctx, member:discord.User = None):#Promotes a member
    if "459287625187065856" in [role.id for role in ctx.message.author.roles] or "459287454172839936" in [role.id for role in ctx.message.author.roles]:
        if member is None:#No member given
            await bot.say("You need to specify a player to promote.")
        elif "459284483066298370" in [role.id for role in member.roles]:#Promotion to member
            await bot.add_roles(member, discord.utils.get(ctx.message.server.roles, name = "[Member]"))#Adds the member role
            channel = member.server.get_channel("460176240238788618")#Gets the player-changes channel
            msg = "{0.mention} has been promoted to Member! :clap: :clap:"
            await bot.send_message(channel, msg.format(member))#Congratulations message
            await bot.send_message(member, "Congratulations on being promoted to Member! :clap:")
            await bot.remove_roles(member, discord.utils.get(ctx.message.server.roles, name = "[Recruit]"))#Removes the recruit role
        elif "459286268275195934" in [role.id for role in member.roles]:#Promotion to moderator
            await bot.add_roles(member, discord.utils.get(ctx.message.server.roles, name = "[Moderator]"))#Adds mod role
            channel = member.server.get_channel("460176240238788618")
            msg = "{0.mention} has been promoted to Moderator! :clap: :clap:"
            await bot.send_message(channel, msg.format(member))
            await bot.send_message(member, "Congratulations on being promoted to Moderator! :clap:")#Congratulations messae
            await bot.remove_roles(member, discord.utils.get(ctx.message.server.roles, name = "[Member]"))#Removes the member role
        elif "459286610593316864" in [role.id for role in member.roles]:#Promotion to mod +
            await bot.add_roles(member, discord.utils.get(ctx.message.server.roles, name = "[Moderator +]"))#Adds the mod + role
            channel = member.server.get_channel("460176240238788618")
            msg = "{0.mention} has been promoted to Moderator +! :clap: :clap:"
            await bot.send_message(channel, msg.format(member))
            await bot.send_message(member, "Congratulations on being promoted to Moderator +! :clap:")#Congratulations message
            await bot.remove_roles(member, discord.utils.get(ctx.message.server.roles, name = "[Moderator]"))#Removes the mod role
        elif "459286909018046470" in [role.id for role in member.roles]:#Promotion to co leader
            await bot.add_roles(member, discord.utils.get(ctx.message.server.roles, name = "[Co-Leader]"))#Adds the co leader role
            channel = member.server.get_channel("460176240238788618")
            await bot.add_roles(member, discord.utils.get(ctx.message.server.roles, name = "[Public]"))#Adds public role
            msg = "{0.mention} has been promoted to Co-Leader! :clap: :clap:"
            await bot.send_message(channel, msg.format(member))
            await bot.send_message(member, "Congratulations on being promoted to Co-Leader! :clap:")#Congratulations message
            await bot.remove_roles(member, discord.utils.get(ctx.message.server.roles, name = "[Moderator +]"))#Removes the mod + role
        elif "459287110810075156" in [role.id for role in member.roles]:#Promotion to manager
            await bot.add_roles(member, discord.utils.get(ctx.message.server.roles, name = "[Manager]"))#Adds the manager role
            channel = member.server.get_channel("460176240238788618")
            msg = "{0.mention} has been promoted to Manager! :clap: :clap:"
            await bot.send_message(channel, msg.format(member))
            await bot.send_message(member, "Congratulations on being promoted to Manager! :clap:")#Congratulations message
            await bot.remove_roles(member, discord.utils.get(ctx.message.server.roles, name = "[Co-Leader]"))#Removes the co leader role
        elif "459287454172839936" in [role.id for role in member.roles]:#Promotion to leader
            await bot.say("Message Jamie if you want to promote someone to Leader")#Cant promote someone to leader
        
        else:#Cannot promote that person
            await bot.say("You cannot promote that person.")
    else:#Lack of permission
        await bot.say("You do not have permission to use this command.")

@bot.command(pass_context=True)
async def demote(ctx, member:discord.User = None):#Demotes a member
    if "459287625187065856" in [role.id for role in ctx.message.author.roles] or "459287454172839936" in [role.id for role in ctx.message.author.roles]:
        if member is None:#No member is given
            await bot.say("You need to specify a player to demote.")
        elif "459287454172839936" in [role.id for role in member.roles]:#Demotion from manager
            await bot.add_roles(member, discord.utils.get(ctx.message.server.roles, name = "[Co-Leader]"))#Adds the co leader role
            channel = member.server.get_channel("460176240238788618")
            msg = "{0.mention} has been demoted to Co-Leader! :thumbsdown:"
            await bot.send_message(channel, msg.format(member))
            await bot.send_message(member, "Unfortunately you have been demoted to Co-Leader! :thumbsdown:")#Demotion message
            await bot.remove_roles(member, discord.utils.get(ctx.message.server.roles, name = "[Manager]"))#Removes the manager role
        elif "459287110810075156" in [role.id for role in member.roles]:#Demotion from co leader
            await bot.add_roles(member, discord.utils.get(ctx.message.server.roles, name = "[Moderator +]"))#Adds the mod + role
            channel = member.server.get_channel("460176240238788618")
            await bot.remove_roles(member, discord.utils.get(ctx.message.server.roles, name = "[Public]"))#Removes public role
            msg = "{0.mention} has been demoted to Moderator +! :thumbsdown:"
            await bot.send_message(channel, msg.format(member))
            await bot.send_message(member, "Unfortunately you have been demoted to Moderator +! :thumbsdown:")#Demotion message
            await bot.remove_roles(member, discord.utils.get(ctx.message.server.roles, name = "[Co-Leader]"))#Removes co leader role
        elif "459286909018046470" in [role.id for role in member.roles]:#Demotion from mod +
            await bot.add_roles(member, discord.utils.get(ctx.message.server.roles, name = "[Moderator]"))#Adds the mod role
            channel = member.server.get_channel("460176240238788618")
            msg = "{0.mention} has been demoted to Moderator! :thumbsdown:"
            await bot.send_message(channel, msg.format(member))
            await bot.send_message(member, "Unfortunately you have been demoted to Moderator! :thumbsdown:")#Demotion message
            await bot.remove_roles(member, discord.utils.get(ctx.message.server.roles, name = "[Moderator +]"))#Removes the mod + role
        elif "459286610593316864" in [role.id for role in member.roles]:#Demotion from mod
            await bot.add_roles(member, discord.utils.get(ctx.message.server.roles, name = "[Member]"))#Adds the member role
            channel = member.server.get_channel("460176240238788618")
            msg = "{0.mention} has been demoted to Member! :thumbsdown:"
            await bot.send_message(channel, msg.format(member))
            await bot.send_message(member, "Unfortunately you have been demoted to Member! :thumbsdown:")#Demotion message
            await bot.remove_roles(member, discord.utils.get(ctx.message.server.roles, name = "[Moderator]"))#Removes the mod role
        elif "459286268275195934" in [role.id for role in member.roles]:#Demotion from member
            await bot.add_roles(member, discord.utils.get(ctx.message.server.roles, name = "[Recruit]"))#Adds the recruit role
            channel = member.server.get_channel("460176240238788618")
            msg = "{0.mention} has been demoted to Recruit! :thumbsdown:"
            await bot.send_message(channel, msg.format(member))
            await bot.send_message(member, "Unfortunately you have been demoted to Recruit! :thumbsdown:")#Demotion message
            await bot.remove_roles(member, discord.utils.get(ctx.message.server.roles, name = "[Member]"))#Removes the member role
        else:#Cant demote that person
            await bot.say("You cannot demote that person.")
    else:#Lack of permission
        await bot.say("You do not have permission to use this command.")

@bot.command(pass_context=True)
async def endless(ctx, member:discord.User = None):#Adds a member to the faction
    if "459287625187065856" in [role.id for role in ctx.message.author.roles] or "459287454172839936" in [role.id for role in ctx.message.author.roles] or "459287110810075156" in [role.id for role in ctx.message.author.roles]:
        #Must be leader, manager or co leader
        if member is None:#No member given 
            await bot.say("You have to specify a player to add to the faction.")
        elif "459344067369631774" in [role.id for role in member.roles]:#Member already has endless role
            await bot.say("That user is already part of Endless.")
        else:#Person does not have the endless role
            await bot.add_roles(member, discord.utils.get(ctx.message.server.roles, name = "[Endless]"))#Adds the endless role
            channel = member.server.get_channel("460176240238788618")
            msg = "{0.mention} has joined Endless! :thumbsup:"
            await bot.send_message(channel, msg.format(member))
            await bot.send_message(member, "Welcome to Endless! :smiley:\nCheck out the custom bot commands here https://docs.google.com/document/d/10CuYlrBqGDuoSSs8iHh8ovWIM0Tz6KYlozkz3JI1AwA/edit?usp=sharing\n.timezone to add your timezone!\nMake sure to read the faction rules as well!")#Welcome message
            await bot.add_roles(member, discord.utils.get(ctx.message.server.roles, name = "[Recruit]"))#Adds the recruit role
    else:#No permission for command
        await bot.say("You do not have permission to use this command.")

@bot.command(pass_context=True)
async def cannoner(ctx, member:discord.User = None):#Adds or removes the cannoner role
    if "459287625187065856" in [role.id for role in ctx.message.author.roles] or "459287454172839936" in [role.id for role in ctx.message.author.roles] or "459287110810075156" in [role.id for role in ctx.message.author.roles]:
        if member is None:#No member is given
            await bot.say("You need to specify a player to become a canonner.")
        elif "461071693335756810" in [role.id for role in member.roles]:#Member already is a cannoner
            await bot.remove_roles(member, discord.utils.get(ctx.message.server.roles, name = "[Cannoner]"))#Removes the cannoner role
            await bot.say("That person is no longer a cannoner.")
        else:#Member is not already a cannoner
            await bot.add_roles(member, discord.utils.get(ctx.message.server.roles, name = "[Cannoner]"))#Adds the cannoner role
            await bot.say("That person is now a cannoner.")
    else:#Lack of permission
        await bot.say("You do not have permission to use this command.")
    
@bot.command(pass_context=True)
async def tag(ctx):#Displays the faction tag
    await bot.say("ᴱⁿᵈˡᵉˢˢ")

@bot.command(pass_context=True)
async def addtag(ctx = None):#Add the faction tag to name
    if "459344067369631774" in [role.id for role in ctx.message.author.roles]:#Must have endless role
        nick = (ctx.message.author.name+"ᴱⁿᵈˡᵉˢˢ")
        await bot.change_nickname(ctx.message.author, nick)
    else:
        await bot.say("You do not have permission to use this command.")


@bot.command(pass_context=True)
async def nick(ctx, newNick = None):#Changes user nickname
    if "459344067369631774" in [role.id for role in ctx.message.author.roles]:#Must have endless role
        if newNick is None:#No nickname is given
            await bot.say("Nickname has been reset.")
            await bot.change_nickname(ctx.message.author, None)#Resets the nickname
        else:
            await bot.change_nickname(ctx.message.author, newNick)#Changes the nickname
            await bot.say("Nickname has been changed.")
    else:#No permission for command
        await bot.say("You do not have permission to use this command.")

@bot.command(pass_context=True)
async def togglepublic(ctx):#Turns public mode on or off
    if "459287625187065856" in [role.id for role in ctx.message.author.roles] or "459287454172839936" in [role.id for role in ctx.message.author.roles] or "459287110810075156" in [role.id for role in ctx.message.author.roles]:
        if "459676185022955530" in [role.id for role in ctx.message.author.roles]:#Member has the public role
            await bot.remove_roles(ctx.message.author, discord.utils.get(ctx.message.server.roles, name="[Public]"))#Removes the public role
            await bot.say("You now cannot access the public channels.")
        else:#Member does not have the public role
            await bot.add_roles(ctx.message.author, discord.utils.get(ctx.message.server.roles, name="[Public]"))#Adds the public role
            await bot.say("You now have access to the public channels.")
    else:#Lack of permission
        await bot.say("You do not have permission to use this command.")

@bot.command(pass_context=True)
async def friend(ctx, member:discord.User = None):#Adds or removes the friend role
    if "459287625187065856" in [role.id for role in ctx.message.author.roles] or "459287454172839936" in [role.id for role in ctx.message.author.roles] or "459287110810075156" in [role.id for role in ctx.message.author.roles]:
        if member is None:#No member given
            await bot.say("You have to specify a player to add/remove as a friend")
        elif "459820843355340810" in [role.id for role in member.roles]:#Member has friend role already
            await bot.remove_roles(member, discord.utils.get(ctx.message.server.roles, name = "[Friend]"))#Removes friend role
            await bot.say("That person is no longer a friend.")
        else:#Member does not have friend role
            await bot.add_roles(member, discord.utils.get(ctx.message.server.roles, name = "[Friend]"))#Adds the member role
            await bot.say("That person is now a friend.")
    else:#Lack of permission
        await bot.say("You do not have permission to use this command.")

@bot.command(pass_context=True)
async def away(ctx, ign:str = None, time:int = None, *,reason:str = None):#Lets people know they are going away
    if "459344067369631774" in [role.id for role in ctx.message.author.roles]:#Must have endless role
        if ign is None or time is None or reason is None:#No ign or time or reason is given
            await bot.say(".away (ign) (time[days]) (reason)")
        else:#All variables covered
            await bot.say("Absence logged.")#Confirmation of absence
            await bot.send_message(discord.Object(id="459797212965109816"),"**Absence**")#Logs the absence in the 'log' channel
            await bot.send_message(discord.Object(id="459797212965109816"),ign)
            await bot.send_message(discord.Object(id="459797212965109816"),time)
            await bot.send_message(discord.Object(id="459797212965109816"),reason)
            await bot.send_message(discord.Object(id="459797212965109816"),"=======================")
    else:#Lack of permission
        await bot.say("You do not have permission to use this command.")

@bot.command(pass_context=True)
async def box(ctx, ign:str = None, spawner1:str = None, spawner2 = "None", other1:str = "None", other2:str = "None", *, other3:str = "None"):#Requests a box
    if "459344067369631774" in [role.id for role in ctx.message.author.roles]:#Must have endless role
        if ign is None or spawner1 is None:#No base arguments given
            await bot.say(".box (ign) (spawner) (spawner[optional]) (other[optional]) (other[optional]) (other[optional])")           
        else:
            await bot.say("Box request logged.")#Logs the request in a separate channel
            await bot.send_message(discord.Object(id="461074799070806016"),"IGN: "+ign)
            await bot.send_message(discord.Object(id="461074799070806016"),"Spawner: "+spawner1)
            await bot.send_message(discord.Object(id="461074799070806016"),"Spawner: "+spawner2)
            await bot.send_message(discord.Object(id="461074799070806016"),"Other: "+other1)
            await bot.send_message(discord.Object(id="461074799070806016"),"Other: "+other2)
            await bot.send_message(discord.Object(id="461074799070806016"),"Other: "+other3)
            await bot.send_message(discord.Object(id="461074799070806016"),"=======================")
    else:#Lack of permission
        await bot.say("You do not have permission to use this coammand.")

@bot.command(pass_context=True)
async def timezone(ctx, timezone:str = None):#Adds a timezone
    if "459344067369631774" in [role.id for role in ctx.message.author.roles]:#Must have the endless role
        #If member already has a timezone
        if "461932068624924693" in [role.id for role in ctx.message.author.roles] or "461931807001018378" in [role.id for role in ctx.message.author.roles] or "461931752148041787" in [role.id for role in ctx.message.author.roles] or "461932516325064717" in [role.id for role in ctx.message.author.roles]:
            await bot.say("You already have a timezone, if you want to change, message Jamie.")
        elif timezone is None:#No timezone given
            await bot.say("The timezones are:    EU    AU    CA    US")
        elif timezone == "EU" or timezone == "eu":
            await bot.add_roles(ctx.message.author, discord.utils.get(ctx.message.server.roles, name ="[EU]"))#Adds EU timezone
            await bot.say("Timezone added.")
        elif timezone == "AU" or timezone == "au":
            await bot.add_roles(ctx.message.author, discord.utils.get(ctx.message.server.roles, name ="[AU]"))#Adds AU timezone
            await bot.say("Timezone added.")
        elif timezone == "CA" or timezone == "CA":
            await bot.add_roles(ctx.message.author, discord.utils.get(ctx.message.server.roles, name ="[CA]"))#Adds CA timezone
            await bot.say("Timezone added.")
        elif timezone == "US" or timezone == "US":
            await bot.add_roles(ctx.message.author, discord.utils.get(ctx.message.server.roles, name ="[US]"))#Adds US timezone
            await bot.say("Timezone added.")
        else:#Role is not a timezone
            await bot.say("That cannot be added as a timezone. The timezones are:    EU    AU    CA    US")
    else:#Lack of permission
        await bot.say("You do not have permission to use this command.")

@bot.command(pass_context=True)
async def buycraft(ctx):
    if "459344067369631774" in [role.id for role in ctx.message.author.roles]:#Must have the endless role
        await bot.say("https://shop.decimatepvp.com/")
    else:
        await bot.say("You do not have permission to use this command.")

@bot.command(pass_context=True)
async def forums(ctx):
    if "459344067369631774" in [role.id for role in ctx.message.author.roles]:#Must have the endless role
        await bot.say("https://www.decimatepvp.com/forums/")
    else:
        await bot.say("You do not have permission to use this command.")

@bot.command(pass_context=True)
async def ip(ctx):
    if "459344067369631774" in [role.id for role in ctx.message.author.roles]:#Must have the endless role
        await bot.say("play.decimatepvp.com")
    else:
        await bot.say("You do not have permission to use this command.")

@bot.command(pass_context=True)
async def usage(ctx):
    await bot.say("https://docs.google.com/document/d/10CuYlrBqGDuoSSs8iHh8ovWIM0Tz6KYlozkz3JI1AwA/edit?usp=sharing")




                            
bot.loop.create_task(wallchecking())
#Bot token
bot.run("NDU5NDI2MTk0MzY3MDUzODcy.Dg2CCg.rWnS8FmLlD3NaPA5rwVqH6YlTts")
