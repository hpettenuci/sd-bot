import random
import os
from discord.ext.commands import Bot
from discord import Game


class DiscordBot():
    BOT = Bot(command_prefix="!")
    DISCORD_TOKEN = None
    TEXT_PREFIX = None

    errorHandleMessages = {
        1000: "Error to get Discord Token",
        1001: "Text Prefix not set! Using default value",
        1002: "Error to start Discord Bot"
    }

    def __init__(self):
        if (self.setDiscordToken() and self.setTextPrefix()):
            self.configBot()

    @staticmethod
    def getBot():
        return DiscordBot.BOT

    @staticmethod
    def throwDices(diceQty, fearDice, bonusDice):
        diceQty = int(diceQty)
        fearDice = int(fearDice)
        bonusDice = int(bonusDice)

        diceCount = 0
        fearCount = 0
        returnMessage = "Result:\n"

        if (diceQty < 1):
            returnMessage = "# Invalid dice quantity"
            return returnMessage
        if (fearDice < 1):
            fearDice = 1
        if (bonusDice < 0):
            bonusDice = 0
        elif bonusDice > 2:
            returnMessage = "# Invalid bonus value!"
            return returnMessage

        while diceCount < diceQty:
            diceResult = random.randint(1, 6)
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
        pass

        return returnMessage

    def setDiscordToken(self):
        try:
            self.DISCORD_TOKEN = os.environ["DISCORD_TOKEN"]
            return True
        except KeyError:
            print(self.errorHandleMessages[1000])
            return False

    def setTextPrefix(self):
        try:
            self.TEXT_PREFIX = os.environ["TEXT_PREFIX"]
            return True
        except KeyError:
            self.TEXT_PREFIX = "!sd-"
            print(self.errorHandleMessages[1001])
            return True

    def configBot(self):
        self.BOT.command_prefix = self.TEXT_PREFIX

    def startBot(self):
        try:
            if (self.DISCORD_TOKEN != ""):
                self.BOT.run(self.DISCORD_TOKEN)
            else:
                print(self.errorHandleMessages[1000])
                return False
        except:
            print(self.errorHandleMessages[1002])
            return False

    @staticmethod
    @BOT.event
    async def on_ready():
        await DiscordBot.getBot().change_presence(activity=Game(name="The ShotGun Diaries RPG"))
        print("Bot Online!")

    @staticmethod
    @BOT.event
    async def on_command_error(ctx, error):
        print(ctx.message)
        print(ctx.command)
        returnMessage = "- Command Error " + ctx.prefix + ctx.command.name + \
                        "\n- Type !sd-help " + ctx.command.name + " to get instructions!"
        await ctx.channel.send(ctx.message.author.mention + "\n" + "```diff\n" + returnMessage + "\n```")

    @staticmethod
    @BOT.command(name="resource",
                 brief="Throw Resource Dices",
                 description="!sd-resource <qty of fear dices> <qty of bonus>",
                 aliases=["r"],
                 pass_context=True)
    async def sdResource(ctx, fearDice, bonusDice):
        if(ctx.message.author.bot):
            return
        if(ctx.message.channel.type == "dm"):
            return

        await ctx.channel.send(ctx.message.author.mention + "\n" + "```diff\n" +
                               DiscordBot.throwDices(4, int(fearDice), int(bonusDice)) + "\n```")

    @staticmethod
    @BOT.command(name="action",
                 brief="Throw action dices",
                 description="!sd-action - <qty of action dices> <qty fear dices> <qty of bonus>",
                 aliases=["a"],
                 pass_context=True)
    async def sdAction(ctx, diceQty, fearDice, bonusDice):
        if(ctx.message.author.bot):
            return
        if(ctx.message.channel.type == "dm"):
            return

        await ctx.channel.send(ctx.message.author.mention + "\n" + "```diff\n" +
                               DiscordBot.throwDices(int(diceQty), int(fearDice), int(bonusDice)) + "\n```")
