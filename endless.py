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
    activity = discord.Game(name=".check")#Changes 'playing' to this
    await bot.change_presence(game = activity)
    print("Logged in as " + bot.user.name)#Trivial log message for startup
    print("ID: " + bot.user.id)#Prints the id of the bot

async def wallchecking():
    await bot.wait_until_ready()#Waits until the bot is ready to take commands
    global wallsOn#Calls the global variables
    global wallsTime
    global count
    channel = discord.Object(id="464193413059969034")#Gets the walls channel id
    message = "<@&417725000494088232> check walls!"#Mentions the 'Endless' role
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
    if "417725000494088232" in [role.id for role in ctx.message.author.roles]:#Must have endless role
        if wallsOn == True:#Checks wall checking is turned on
            count = 0#Count is reset to 0
            await bot.say(ctx.message.author.mention+" has checked walls!")#Confirmation message
        else:#If wall checking is turned off
            await bot.say("Wall checking is not currently turned on.")
    else:#Lack of permission
        await bot.say("You do not have permission to use this command.")

@bot.command(pass_context=True)
async def weewoo(ctx, side:str = None):
    if "417725000494088232" in [role.id for role in ctx.message.author.roles]:#Must have endless role
        channel = discord.Object(id="464193413059969034")
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
    if "417743037926735873" in [role.id for role in ctx.message.author.roles]:#Must be leader
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
    if "417743037926735873" in [role.id for role in ctx.message.author.roles]:#Must be leader
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
async def usage(ctx):
    await bot.say("https://docs.google.com/document/d/10CuYlrBqGDuoSSs8iHh8ovWIM0Tz6KYlozkz3JI1AwA/edit?usp=sharing")




                            
bot.loop.create_task(wallchecking())
#Bot token
bot.run("NDU5NDI2MTk0MzY3MDUzODcy.Dg2CCg.rWnS8FmLlD3NaPA5rwVqH6YlTts")
