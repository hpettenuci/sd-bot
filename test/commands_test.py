from sd_bot.bot_commands import (
    check_message_origin,
    cmd_error,
    cmd_resource,
    cmd_action
)

class TestCommands:
    def test_cmd_error(self):
        author = "test"
        prefix = "!sd-"
        cmd_name = "action"
        cmd_return = cmd_error(author, prefix, cmd_name)
        assert author in cmd_return

    def test_cmd_resource(self):
        author = "test"
        fear_dice = 1
        bonus_dice = 0
        cmd_return = cmd_resource(author, fear_dice, bonus_dice)
        assert author in cmd_return

    def test_cmd_action(self):
        author = "test"
        dice_qty = 4
        fear_dice = 1
        bonus_dice = 0
        cmd_return = cmd_action(author, dice_qty, fear_dice, bonus_dice)
        assert author in cmd_return