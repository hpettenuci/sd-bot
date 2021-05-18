from sd_bot.rpgrules.dicer import Dicer

RETURN_MESSAGE_PREFIX = "```diff\n"
RETURN_MESSAGE_SUFIX = "\n```"

def check_message_origin(ctx) -> bool:
    if ctx.message.author.bot or ctx.message.channel.type == "dm":
        return False
    else:
        return True

def cmd_error(author: str, prefix: str, cmd_name: str):
    return author + "\n" + RETURN_MESSAGE_PREFIX \
        + "- Command Error " + prefix + cmd_name \
        + "\n- Type !sd-help " + cmd_name + " to get instructions!" \
        + RETURN_MESSAGE_SUFIX

def cmd_resource(author: str, fear_dice: str, bonus_dice: str):
    dicer = Dicer()
    return author + "\n" + RETURN_MESSAGE_PREFIX \
        + dicer.execute_action(4, int(fear_dice), int(bonus_dice)) \
        + RETURN_MESSAGE_SUFIX

def cmd_action(author: str, dice_qty: str, fear_dice: str, bonus_dice: str):
    dicer = Dicer()
    return author + "\n" + RETURN_MESSAGE_PREFIX \
        + dicer.execute_action(int(dice_qty), int(fear_dice), int(bonus_dice)) \
        + RETURN_MESSAGE_SUFIX