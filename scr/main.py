import random
from configparser import ConfigParser
from discord.ext.commands import Bot
from discord import Game

def getConfig(filename='../config/sd-bot.config', section='general'):
    # create a parser
    parser = ConfigParser()
    # read config file
    parser.read(filename)
 
    # get section, default to general
    config = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            config[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))
 
    return config

CONFIG = getConfig(section="general")
sdBot = Bot(command_prefix=CONFIG["prefix"])

@sdBot.event
async def on_ready():
    await sdBot.change_presence(activity=Game(name="The ShotGun Diaries"))
    print("Bot Online!")
    
@sdBot.event
async def on_command_error(ctx,error):   
    print(ctx.message)
    print(ctx.command)
    returnMessage = "- Command Error " + ctx.prefix + ctx.command.name + "\n- Type !sd-help " + ctx.command.name + " to get instructions!"
    await ctx.channel.send(ctx.message.author.mention + "\n" +  "```diff\n" + returnMessage + "\n```")

@sdBot.command( name="resource",
                brief="Throw Resource Dices",
                description="!sd-recurso <qty of fear dices> <qty of bonus>",
                aliases=["r"],
                pass_context=True)
async def sdResource(ctx, fearDice, bonusDice):
        if(ctx.message.author.bot): return
        if(ctx.message.channel.type == "dm"): return

        diceQty     = 4
        fearDice    = int(fearDice)
        bonusDice   = int(bonusDice)

        diceCount   = 0
        fearCount   = 0
        
        returnMessage = "Result:\n"

        if (fearDice < 1):
            fearDice = 1
        if (bonusDice < 0):
            bonusDice = 0
        elif bonusDice > 2:
            returnMessage = "# Invalid bonus value!"
            await ctx.channel.send(ctx.message.author.mention + "\n" +  "```diff\n" + returnMessage + "\n```")
            return


        while diceCount < diceQty:
            diceResult = random.randint(1,6)
            diceResult = diceResult + bonusDice
            if (diceResult > 6):
                diceResult = 6

            if (fearCount < fearDice):
                returnMessage = returnMessage + "- " + str(diceResult) + "\n"
                fearCount += 1
            else:
                if (diceResult == 6):
                    returnMessage = returnMessage + "+ " + str(diceResult) + "\n"
                else:
                    returnMessage = returnMessage + "# " + str(diceResult) + "\n"

            diceCount += 1            
        
        await ctx.channel.send(ctx.message.author.mention + "\n" +  "```diff\n" + returnMessage + "\n```")
    
@sdBot.command( name="action",
                brief="Throw action dices",
                description="!sd-action - <qty of action dices> <qty fear dices> <qty of bonus>",
                aliases=["a"],
                pass_context=True)
async def sdAction(ctx, diceQty, fearDice, bonusDice):
        if(ctx.message.author.bot): return
        if(ctx.message.channel.type == "dm"): return

        diceQty     = int(diceQty)
        fearDice    = int(fearDice)
        bonusDice   = int(bonusDice)

        diceCount   = 0
        fearCount   = 0
        
        returnMessage = "Result:\n"

        if (fearDice < 1):
            fearDice = 1
        if (bonusDice < 0):
            bonusDice = 0
        elif bonusDice > 2:
            returnMessage = "# Invalid bonus value!"
            await ctx.channel.send(ctx.message.author.mention + "\n" +  "```diff\n" + returnMessage + "\n```")
            return


        while diceCount < diceQty:
            diceResult = random.randint(1,6)
            diceResult = diceResult + bonusDice
            if (diceResult > 6):
                diceResult = 6

            if (fearCount < fearDice):
                returnMessage = returnMessage + "- " + str(diceResult) + "\n"
                fearCount += 1
            else:
                if (diceResult == 6):
                    returnMessage = returnMessage + "+ " + str(diceResult) + "\n"
                else:
                    returnMessage = returnMessage + "# " + str(diceResult) + "\n"

            diceCount += 1            
        
        await ctx.channel.send(ctx.message.author.mention + "\n" +  "```diff\n" + returnMessage + "\n```")
    


sdBot.run(CONFIG["token"])