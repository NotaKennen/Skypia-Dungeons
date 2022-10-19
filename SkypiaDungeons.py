#  with open(os.path.expanduser(f'~/Downloads/Code Projects/Skypia Verification bot/Card game/People/{ctx.author}.json')) as f:
#        data = json.load(f)
#        Cardmoney = data["Money"]

# Load X


from statistics import mode
import discord
from discord.ext import commands
from discord.utils import get
import praw
from datetime import datetime
import json
import os
import random
import asyncio

print("Skypia Dungeons")
print("Coded by Memarios")
print("----------------------------------------------")

bot = commands.Bot(command_prefix='§')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('----------------------------------------------')

with open(os.path.expanduser(f'~/Documents/Code Projects/Skypia Dungeons/gitignored/token.json')) as f:
    data = json.load(f)
    DiscToken = data["Token"]

@bot.command()
async def register(ctx):
    person = {
    "Money": 0}
    json_object = json.dumps(person, indent=1)
    with open(os.path.expanduser(f'~/Documents/Code Projects/Skypia Dungeons/Database/People/Money/{ctx.author}.json'), "w") as outfile:
        outfile.write(json_object)
    person = {
    "Factionname": 0,
    "Factionleader": "false"}
    json_object = json.dumps(person, indent=1)
    with open(os.path.expanduser(f'~/Documents/Code Projects/Skypia Dungeons/Database/People/Factiondata/{ctx.author}.json'), "w") as outfile:
        outfile.write(json_object)
    await ctx.send("You have been registered!")
    await ctx.send("Note that this is the BETA build, all progress may be lost due to an update")

@bot.command()
@commands.cooldown(1, 15, commands.BucketType.user)
async def search(ctx):
    #Loads money
    with open(os.path.expanduser(f'~/Documents/Code Projects/Skypia Dungeons/Database/People/Money/{ctx.author}.json')) as f:
        data = json.load(f)
        Money = data["Money"]

    #list of places
    place = ["a garbagecan", "a couch", "an old lady's purse", "a Minecraft server", "a Stackoverflow thread", "a bank", "an UFO", "the gas station bathroom", "your sink", "a hospital bed", "a fridge", "a college classroom", "the basement pipes", "under the bar stool"]
    placename = (random.choice(place))

    # Randomizes rewards and calculates new money amount
    reward = int(random.randint(10, 70))
    await ctx.send(f"You searched {placename} and found {reward}€")
    Money = Money + reward

    # Sends new money values
    person = {
    "Money": Money}
    json_object = json.dumps(person, indent=1)
    with open(os.path.expanduser(f'~/Documents/Code Projects/Skypia Dungeons/Database/People/Money/{ctx.author}.json'), "w") as outfile:
        outfile.write(json_object)

@bot.command()
async def bal(ctx, name: str=None):
    # Replaces name with author if not mentioned
    if name is None:
        name = ctx.author

    # Loads money
    with open(os.path.expanduser(f'~/Documents/Code Projects/Skypia Dungeons/Database/People/Money/{name}.json')) as f:
        data = json.load(f)
        Money = data["Money"]
    await ctx.send(f"{name} has {Money}€")

@bot.command()
async def shop(ctx):
    # Loads items from shop.json
    with open(os.path.expanduser(f'~\Documents\Code Projects\Skypia Dungeons\Database\Shop\shop.json')) as f:
        data = json.load(f)
        item1 = data["item1"]
        item2 = data["item2"]
        item3 = data["item3"]
        item4 = data["item4"]
        item1price = data["item1price"]
        item2price = data["item2price"]
        item3price = data["item3price"]
        item4price = data["item4price"]
    
    # Sends embed w items
    embed=discord.Embed(title="----------------------", description="Shop by Memco™", color=0x41c882)
    embed.set_author(name="Shop")
    embed.add_field(name=f"1. {item1}", value=f"{item1price}€", inline=False)
    embed.add_field(name=f"2. {item2}", value=f"{item2price}€", inline=False)
    embed.add_field(name=f"3. {item3}", value=f"{item3price}€", inline=False)
    embed.add_field(name=f"4. {item4}", value=f"{item4price}€", inline=False)
    embed.set_footer(text="Use §buy (item number) to buy stuff")
    await ctx.send(embed=embed)

@bot.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def coinflip(ctx, amount: int=None):
    # Loads money
    with open(os.path.expanduser(f'~/Documents/Code Projects/Skypia Dungeons/Database/People/Money/{ctx.author}.json')) as f:
        data = json.load(f)
        Money = data["Money"]
    # Checks arguments
    if amount is None:
            await ctx.send("You need to select an amount to play with")
    else:
        if Money < amount:
            await ctx.send("You can't play with more money than you have")
        else:
            chances = random.randint(1,20)
            if chances <= 10:
                await ctx.send(f"You won {amount}€")
                Money = Money + amount
                person = {
                "Money": Money}
                json_object = json.dumps(person, indent=1)
                with open(os.path.expanduser(f'~/Documents/Code Projects/Skypia Dungeons/Database/People/Money/{ctx.author}.json'), "w") as outfile:
                    outfile.write(json_object)
            elif chances >= 11:
                await ctx.send(f"You lost!")
                Money = Money - amount
                person = {
                "Money": Money}
                json_object = json.dumps(person, indent=1)
                with open(os.path.expanduser(f'~/Documents/Code Projects/Skypia Dungeons/Database/People/Money/{ctx.author}.json'), "w") as outfile:
                    outfile.write(json_object)
            else:
                await ctx.send("Ayo something went wrong")

@bot.command()
async def blackjack(ctx, amount: int=None):
    if amount is None:
        ctx.send("You need to select an amount to play with")
    else: 
        # Loads money
        with open(os.path.expanduser(f'~/Documents/Code Projects/Skypia Dungeons/Database/People/Money/{ctx.author}.json')) as f:
            data = json.load(f)
        Money = data["Money"]
        if amount > Money:
            await ctx.send("You can't play with more money than you have")
        else:
            await ctx.send("Sorry WIP")

@bot.command()
async def buy(ctx, item: int=None, amount: int=None):
    # Loads shop.json and Money
    with open(os.path.expanduser(f'~\Documents\Code Projects\Skypia Dungeons\Database\Shop\shop.json')) as f:
        data = json.load(f)
        item1 = data["item1"]
        item2 = data["item2"]
        item3 = data["item3"]
        item4 = data["item4"]
        item1price = data["item1price"]
        item2price = data["item2price"]
        item3price = data["item3price"]
        item4price = data["item4price"]
    with open(os.path.expanduser(f'~/Documents/Code Projects/Skypia Dungeons/Database/People/Money/{ctx.author}.json')) as f:
        data = json.load(f)
        Money = data["Money"]

    # Checks what item user is trying to buy
    if amount is None:
        amount = 1
    if item is None:
        item = 0
    if item == 1:
        item = item1
        itemprice = item1price
    elif item == 2:
        item = item2
        itemprice = item2price
    elif item == 3:
        item = item3
        itemprice = item3price
    elif item == 4:
        item = item4
        itemprice = item4price

    if item == 0:
        # Sends message if user hasn't selected an item to buy
        await ctx.send("You need to select an item")
    elif Money <= itemprice:
        # Sends message if user doesnt have enough money
        await ctx.send(f"You need {itemprice - Money}€ more to buy this item")
    else:
        # Calculates the new money amount 
        # Sends the new money amount to database
        # (WIP) Gives user the item
        # Sends message to user
        Money = Money - itemprice
        person = {
        "Money": Money}
        json_object = json.dumps(person, indent=1)
        with open(os.path.expanduser(f'~/Documents/Code Projects/Skypia Dungeons/Database/People/Money/{ctx.author}.json'), "w") as outfile:
            outfile.write(json_object)
        await ctx.send(f'Succesfully bought "{item}"!')

@bot.command()
async def f(ctx, action: str=None, facname: str=None):
    #loads up personal Fac file
    with open(os.path.expanduser(f'~/Documents/Code Projects/Skypia Dungeons/Database/People/Factiondata/{ctx.author}.json')) as f:
        data = json.load(f)
        leadername = data["factionname"]
        leader = data["Leader"]
    
    #checks for Nones
    if action is None:
        await ctx.send("You need to select what you want to do")
    elif action == "create":
        #checks for Nones and also if the player is already a fac leader
        if facname is None:
            await ctx.send("You need to select a name for your faction")
        elif leader == "true":
            await ctx.send(f'You are already a leader of {leadername}')
        else:
            # makes a faction data in Factions folder
            person = {
            "Name": facname,
            "Leader": ctx.author}
            json_object = json.dumps(person, indent=1)
            with open(os.path.expanduser(f'~/Documents/Code Projects/Skypia Dungeons/Database/Factions/{facname}.json'), "w") as outfile:
                outfile.write(json_object)
            
            # makes you a leader in the personal factions folder
            person = {
            "Factionname": f"{facname}",
            "Factionleader": "true"
            }
            json_object = json.dumps(person, indent=1)
            with open(os.path.expanduser(f'~/Documents/Code Projects/Skypia Dungeons/Database/People/Factiondata/{ctx.author}.json'), "w") as outfile:
                outfile.write(json_object)
            await ctx.send(f'A Faction with the name of "{facname}" has been created')
    else:
        await ctx.send("You need to select what you want to do")

@bot.event
async def on_command_error(ctx, error):
  if isinstance(error, commands.CommandOnCooldown):
    await ctx.send(f"Ayo slow down a little! You can use it again in {round(error.retry_after, 2)} seconds.")


bot.run(DiscToken)