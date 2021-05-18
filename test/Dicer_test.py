import re

import pytest

from sd_bot.rpgrules.dicer import Dicer


class TestDicer:
    dicer = Dicer()

    def test_dice_qty_error(self):
        with pytest.raises(ValueError) as excinfo:
            self.dicer.validate_dice_qty(0)
        assert "Invalid dice quantity" in str(excinfo.value)

    def test_dice_qty_ok(self):
        self.dicer.validate_dice_qty(1)

    def test_min_fear(self):
        fear_dice = self.dicer.validate_fear_dice(0)
        assert fear_dice == 1

    def test_fear(self):
        fear_dice = self.dicer.validate_fear_dice(2)
        assert fear_dice == 2

    def test_min_bonus(self):
        bonus_dice = self.dicer.validate_bonus_dice(-1)
        assert bonus_dice == 0

    def test_bonus(self):
        bonus_dice = self.dicer.validate_bonus_dice(2)
        assert bonus_dice == 2

    def test_error_bonus(self):
        with pytest.raises(ValueError) as excinfo:
            self.dicer.validate_bonus_dice(3)
        assert "Invalid bonus value" in str(excinfo.value)

    def test_dice_value(self):
        dice_result = self.dicer.throw_dice(7)
        assert 1 <= dice_result <= 6

    def test_format_success(self):
        dice_result = self.dicer.format_result(6)
        assert re.search(r"\+ [1-6]", dice_result)

    def test_format_convetional(self):
        dice_result = self.dicer.format_result(1)
        assert re.search(r"# [1-6]", dice_result)

    def test_format_fear(self):
        dice_result = self.dicer.set_dice_as_fear(1)
        assert re.search(r"- [1-6]", dice_result)

    def test_action_dice_error(self):
        with pytest.raises(ValueError) as excinfo:
            self.dicer.execute_action(0, 0, 0)
        assert "Invalid dice quantity" in str(excinfo.value)

    def test_action_bonus_error(self):
        with pytest.raises(ValueError) as excinfo:
            self.dicer.execute_action(1, 0, 3)
        assert "Invalid bonus value" in str(excinfo.value)

    def test_action_min_fear(self):
        dice_result = self.dicer.execute_action(1, 0, 0)
        assert re.search(r"- [1-6]", dice_result)

    def test_action_fear(self):
        fear_qty = 2
        dice_result = self.dicer.execute_action(3, fear_qty, 0)
        fear_result = re.findall(r"- [1-6]", dice_result)
        assert len(fear_result) == fear_qty

    def test_action_five_dices(self):
        dice_qty = 5
        dice_result = self.dicer.execute_action(dice_qty, 0, 0)
        fear_result = re.findall(r"- [1-6]", dice_result)
        success_result = re.findall(r"\+ [1-6]", dice_result)
        conventional_result = re.findall(r"# [1-6]", dice_result)
        assert (
            len(fear_result) + len(success_result) + len(conventional_result)
            == dice_qty
        )
