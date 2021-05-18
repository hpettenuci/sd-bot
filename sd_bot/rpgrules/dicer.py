import random
import sys

from sd_bot.common.logger import BotLogger


class Dicer:
    log_lib = BotLogger()
    logger = log_lib.logging_override(__name__)
    sys.excepthook = log_lib.exception_handler

    @staticmethod
    def validate_dice_qty(dice_qty: int):
        if dice_qty < 1:
            raise ValueError("#Invalid dice quantity")

    @staticmethod
    def validate_fear_dice(fear_dice: int) -> int:
        if fear_dice < 1:
            fear_dice = 1
        return fear_dice

    @staticmethod
    def validate_bonus_dice(bonus_dice: int) -> int:
        if bonus_dice < 0:
            bonus_dice = 0
        elif bonus_dice > 2:
            raise ValueError("#Invalid bonus value")
        return bonus_dice

    @staticmethod
    def throw_dice(bonus_dice: int) -> int:
        dice_result = random.randint(1, 6) + bonus_dice
        if dice_result > 6:
            dice_result = 6
        return dice_result

    @staticmethod
    def format_result(dice_value: int) -> str:
        if dice_value == 6:
            return_message = "+ " + str(dice_value) + "\n"
        else:
            return_message = "# " + str(dice_value) + "\n"
        return return_message

    @staticmethod
    def set_dice_as_fear(dice_value: int) -> str:
        return "- " + str(dice_value) + "\n"

    @staticmethod
    def execute_action(dice_qty: int, fear_dice: int, bonus_dice: int) -> str:
        try:
            dice_count = 0
            fear_count = 0
            return_message = "Result:\n"

            Dicer.validate_dice_qty(dice_qty)
            fear_dice = Dicer.validate_fear_dice(fear_dice)
            bonus_dice = Dicer.validate_bonus_dice(bonus_dice)

            while dice_count < dice_qty:
                dice_value = Dicer.throw_dice(bonus_dice)

                if fear_count < fear_dice:
                    return_message = return_message + Dicer.set_dice_as_fear(dice_value)
                    fear_count += 1
                else:
                    return_message = return_message + Dicer.format_result(dice_value)

                dice_count += 1

            return return_message
        except Exception as error:
            Dicer.logger.info(error)
            raise error
