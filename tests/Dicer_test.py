import re
import pytest
from src.common.Dicer import Dicer


class TestDicer():
    dicer = Dicer()

    def test_DiceQtyError(self):
        with pytest.raises(ValueError) as excinfo:   
            self.dicer.validateDiceQty(0)
            assert 'Invalid dice quantity' in str(excinfo.value)

    def test_DiceQtyOk(self):
        self.dicer.validateDiceQty(1)            

    def test_MinFear(self):
        fearDice = self.dicer.validateFearDice(0)
        assert fearDice == 1

    def test_Fear(self):
        fearDice = self.dicer.validateFearDice(2)
        assert fearDice == 2

    def test_MinBonus(self):
        bonusDice = self.dicer.validateBonusDice(-1)
        assert bonusDice == 0

    def test_Bonus(self):
        bonusDice = self.dicer.validateBonusDice(2)
        assert bonusDice == 2

    def test_ErrorBonus(self):
        with pytest.raises(ValueError) as excinfo:   
            self.dicer.validateBonusDice(3)
            assert 'Invalid bonus value' in str(excinfo.value)

    def test_DiceValue(self):
        diceResult = self.dicer.throwDice(7)
        assert 1 <= diceResult <= 6

    def test_FormatSuccess(self):
        diceResult = self.dicer.formatResult(6)
        assert re.search(r"\+ [1-6]", diceResult)

    def test_FormatConvetional(self):
        diceResult = self.dicer.formatResult(1)
        assert re.search(r"# [1-6]", diceResult)

    def test_FormatFear(self):
        diceResult = self.dicer.setDiceAsFear(1)
        assert re.search(r"- [1-6]", diceResult)

    def test_ActionDiceError(self):
        with pytest.raises(ValueError) as excinfo:
            self.dicer.executeAction(0,0,0)
            assert 'Invalid dice quantity' in str(excinfo.value)

    def test_ActionBonusError(self):
        with pytest.raises(ValueError) as excinfo:
            self.dicer.executeAction(1,0,3)
            assert 'Invalid bonus value' in str(excinfo.value)

    def test_ActionMinFear(self):
        diceResult = self.dicer.executeAction(1,0,0)
        assert re.search(r"- [1-6]", diceResult)

    def test_ActionFear(self):
        fearQty = 2
        diceResult = self.dicer.executeAction(3,fearQty,0)
        fearResult = re.findall(r"- [1-6]", diceResult)
        assert len(fearResult) == fearQty

    def test_ActionFiveDices(self):
        diceQty = 5
        diceResult = self.dicer.executeAction(diceQty,0,0)
        fearResult = re.findall(r"- [1-6]", diceResult)
        successResult = re.findall(r"\+ [1-6]", diceResult)
        conventionalResult = re.findall(r"# [1-6]", diceResult)
        assert len(fearResult) + len(successResult) + len(conventionalResult) == diceQty