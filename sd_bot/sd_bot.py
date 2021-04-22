import os
import sys

from discord import Game
from discord.ext.commands import Bot

from sd_bot.common.Logger import Logger
from sd_bot.dicer.Dicer import Dicer


class DiscordBot:
    logLib = Logger()
    logger = logLib.loggingOverride(__name__)
    sys.excepthook = logLib.exception_handler

    dicer = Dicer()

    BOT = Bot(command_prefix="!")
    DISCORD_TOKEN = None
    TEXT_PREFIX = None

    errorHandleMessages = {
        1000: "Error to get Discord Token",
        1001: "Text Prefix not set! Using default value",
        1002: "Error to start Discord Bot",
        1003: "Command Error",
    }

    def __init__(self):

        self.setDiscordToken()
        self.setTextPrefix()
        self.configBot()

    @staticmethod
    def getBot():
        return DiscordBot.BOT

    def setDiscordToken(self):
        try:
            self.DISCORD_TOKEN = os.environ["DISCORD_TOKEN"]
        except KeyError:
            errorMessage = self.errorHandleMessages[1000]
            self.logger.error(errorMessage)
            raise KeyError(errorMessage)

    def setTextPrefix(self):
        try:
            self.TEXT_PREFIX = os.environ["TEXT_PREFIX"]
        except KeyError:
            self.TEXT_PREFIX = "!sd-"
            self.logger.info(self.errorHandleMessages[1001])

    def configBot(self):
        self.BOT.command_prefix = self.TEXT_PREFIX

    def startBot(self):
        try:
            errorMessage = ""
            if self.DISCORD_TOKEN != "":
                self.BOT.run(self.DISCORD_TOKEN)
            else:
                errorMessage = self.errorHandleMessages[1000]
                self.logger.error(errorMessage)
                raise Exception(errorMessage)
        except Exception:
            if errorMessage == "":
                errorMessage = self.errorHandleMessages[1002]
            self.logger.error(errorMessage)
            raise Exception(errorMessage)

    @staticmethod
    @BOT.event
    async def on_ready():
        await DiscordBot.getBot().change_presence(
            activity=Game(name="The ShotGun Diaries RPG")
        )
        DiscordBot.logger.info("Bot Online!")

    @staticmethod
    @BOT.event
    async def on_command_error(ctx, error):
        DiscordBot.logger.info(
            DiscordBot.errorHandleMessages[1003],
            extra={"command": ctx.command.name, "error": error},
        )

        returnMessage = (
            "- Command Error "
            + ctx.prefix
            + ctx.command.name
            + "\n- Type !sd-help "
            + ctx.command.name
            + " to get instructions!"
        )
        await ctx.channel.send(
            ctx.message.author.mention + "\n" + "```diff\n" + returnMessage + "\n```"
        )

    @staticmethod
    @BOT.command(
        name="resource",
        brief="Throw Resource Dices",
        description="!sd-resource < qty of fear dices > < qty of bonus - between 0 and 2 >",
        aliases=["r"],
        pass_context=True,
    )
    async def sdResource(ctx, fearDice, bonusDice):
        if ctx.message.author.bot:
            return
        if ctx.message.channel.type == "dm":
            return

        await ctx.channel.send(
            ctx.message.author.mention
            + "\n"
            + "```diff\n"
            + DiscordBot.dicer.executeAction(4, int(fearDice), int(bonusDice))
            + "\n```"
        )

    @staticmethod
    @BOT.command(
        name="action",
        brief="Throw action dices",
        description="!sd-action - <qty of action dices - greater than 0 > <qty fear dices > < qty of bonus - between 0 and 2 >",
        aliases=["a"],
        pass_context=True,
    )
    async def sdAction(ctx, diceQty, fearDice, bonusDice):
        if ctx.message.author.bot:
            return
        if ctx.message.channel.type == "dm":
            return

        await ctx.channel.send(
            ctx.message.author.mention
            + "\n"
            + "```diff\n"
            + DiscordBot.dicer.executeAction(
                int(diceQty), int(fearDice), int(bonusDice)
            )
            + "\n```"
        )
