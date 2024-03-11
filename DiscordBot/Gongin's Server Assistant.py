import datetime
import asyncio
import os
import socket

#Imports for discord
from nextcord.ext import commands
from nextcord import ButtonStyle, Interaction, Intents, SlashOption
from nextcord.ui import Button, View

#Data Varibels for a bot
BOT_TOKEN = ""

#Data for Intets
intents = Intents.default()
intents.message_content = True
intents.members = True
bots = commands.Bot(intents=intents)
bots.remove_command("help")

@bots.slash_command()
async def voting(Interaction:Interaction, needbv3:int, bv3:str, time_s:int, theme:str ):
    #Var for voting
    ListUsed = []
    ListUserYes = []
    ListUserNo = []
    ListUsedBv3 = []
    
    #Create Buttons
    ButtonVoting1 = Button(label="Yes" ,style=ButtonStyle.green)
    ButtonVoting2 = Button(label="No" ,style=ButtonStyle.red)
    
    if needbv3 == 1:
        ButtonVoting3 = Button(label=bv3 ,style=ButtonStyle.blurple)
    

    #Binding Buttons for def 
    async def buttvo1(interaction):
        if interaction.user not in ListUsed:
            ListUsed.append( interaction.user )
            ListUserYes.append( interaction.user )
            await interaction.response.send_message("Correct " + str(interaction.user))
        else:
            await interaction.response.send_message("You can't vote " + str(interaction.user))
            
    async def buttvo2(interaction):
        if interaction.user not in ListUsed:
            ListUsed.append( interaction.user )
            ListUserNo.append( interaction.user )
            await interaction.response.send_message("Correct " + str(interaction.user))
        else:
            await interaction.response.send_message("You can't vote " + str(interaction.user))

    async def buttvo3(interaction):
        if interaction.user not in ListUsed:
            ListUsed.append( interaction.user )
            ListUsedBv3.append( interaction.user )
            await interaction.response.send_message("Correct " + str(interaction.user))
        else:
            await interaction.response.send_message("You can't vote " + str(interaction.user))
            
    ButtonVoting1.callback = buttvo1
    ButtonVoting2.callback = buttvo2
    if needbv3 == 1: 
        ButtonVoting3.callback = buttvo3

    #Createing Views
    voteview = View(timeout=(time_s + 1))
    voteview.add_item(ButtonVoting1)
    voteview.add_item(ButtonVoting2)
    if needbv3 == 1:
        voteview.add_item(ButtonVoting3)
    
    #Starting voting 
    print("Voting " + str(time_s) + " Seconds" + '\n' + "About " + theme)
    await Interaction.response.send_message("This Voting will be for next " + str(time_s) + " Seconds" + '\n' + "This voting is about " + theme, view = voteview)
    
    #Set Timer
    Start = datetime.datetime.now()
    End = Start + datetime.timedelta(seconds=time_s)
    Timer = (End - Start).total_seconds()
    
    #Ending
    ChanelIdVoting = bots.get_channel(1134602984374947922)
   

    #Wating
    await asyncio.sleep(Timer)  
    
    #Message
    await ChanelIdVoting.send("**#Voting Ended#**" + '\n' + "Results: " + '\n' + "For Yes: **" + str(len(ListUserYes)) + "**" ) 
    await ChanelIdVoting.send("For No : **" + str(len(ListUserNo)) + "**")
    
    #Should I send option 3
    if needbv3 == 1:
        await ChanelIdVoting.send("For " + bv3 + ": **" + str(len(ListUsedBv3)) + "**")
        

    await ChanelIdVoting.send("Ended Test")

@bots.event
async def on_ready():
    print("Bot Workin")

if __name__ == '__main__':
    bots.run(BOT_TOKEN)
