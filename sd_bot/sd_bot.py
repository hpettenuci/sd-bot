import os
import sys

from discord import Game
from discord.ext.commands import Bot

from sd_bot.common.logger import BotLogger

from sd_bot.bot_commands import (
    check_message_origin,
    cmd_error,
    cmd_resource,
    cmd_action
)


class DiscordBot:
    log_lib = BotLogger()
    logger = log_lib.logging_override(__name__)
    sys.excepthook = log_lib.exception_handler

    BOT = Bot(command_prefix="!")
    DISCORD_TOKEN = None
    TEXT_PREFIX = None

    ERROR_HANDLE_MESSAGES = {
        1000: "Error to get Discord Token",
        1001: "Text Prefix not set! Using default value",
        1002: "Error to start Discord Bot",
        1003: "Command Error",
    }

    def __init__(self):
        self.set_discord_token()
        self.set_text_prefix()
        self.config_bot()

    @staticmethod
    def get_bot():
        return DiscordBot.BOT

    def set_discord_token(self):
        try:
            self.DISCORD_TOKEN = os.environ["DISCORD_TOKEN"]
        except KeyError:
            error_message = self.ERROR_HANDLE_MESSAGES[1000]
            self.logger.error(error_message)
            raise KeyError(error_message)

    def set_text_prefix(self):
        try:
            self.TEXT_PREFIX = os.environ["TEXT_PREFIX"]
        except KeyError:
            self.TEXT_PREFIX = "!sd-"
            self.logger.info(self.ERROR_HANDLE_MESSAGES[1001])

    def config_bot(self):
        self.BOT.command_prefix = self.TEXT_PREFIX

    def start_bot(self):
        try:
            error_message = ""
            if self.DISCORD_TOKEN != "":
                self.BOT.run(self.DISCORD_TOKEN)
            else:
                error_message = self.ERROR_HANDLE_MESSAGES[1000]
                self.logger.error(error_message)
                raise ValueError(error_message)
        except Exception:
            if error_message == "":
                error_message = self.ERROR_HANDLE_MESSAGES[1002]
            self.logger.error(error_message)
            raise ValueError(error_message)

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
        await ctx.channel.send(
            cmd_error(ctx.message.author.mention, ctx.prefix, ctx.command.name)
        )  

    @staticmethod
    @BOT.command(
        name="resource",
        brief="Throw Resource Dices",
        description="!sd-resource < qty of fear dices > < qty of bonus - between 0 and 2 >",
        aliases=["r"],
        pass_context=True,
    )
    async def sd_resource(ctx, fear_dice, bonus_dice):
        if check_message_origin(ctx):
            await ctx.channel.send(
                cmd_resource(ctx.message.author.mention, fear_dice, bonus_dice)
            )        

    @staticmethod
    @BOT.command(
        name="action",
        brief="Throw action dices",
        description="!sd-action - <qty of action dices - greater than 0 > <qty fear dices > < qty of bonus - between 0 and 2 >",
        aliases=["a"],
        pass_context=True,
    )
    async def sd_action(ctx, dice_qty, fear_dice, bonus_dice):
        if check_message_origin(ctx):
            await ctx.channel.send(
                cmd_action(ctx.message.author.mention, dice_qty, fear_dice, bonus_dice)
            )   