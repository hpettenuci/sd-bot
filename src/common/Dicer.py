import random
import common.Logger as logLib

class Dicer():
    logger = logLib.loggingOverride(__name__)

    @staticmethod    
    def validateDiceQty(diceQty:int):
        if (diceQty < 1):
            raise ValueError("#Invalid dice quantity")

    @staticmethod
    def validateFearDice(fearDice:int) -> int:
        if (fearDice < 1):
            fearDice = 1
        return fearDice

    @staticmethod
    def validateBonusDice(bonusDice:int) -> int:
        if (bonusDice < 0):
            bonusDice = 0
        elif bonusDice > 2:
            raise ValueError("#Invalid bonus value")
        return bonusDice

    @staticmethod
    def throwDice(bonusDice:int) -> int:
        diceResult = random.randint(1, 6) + bonusDice
        if (diceResult > 6):
            diceResult = 6
        return diceResult
        
    @staticmethod
    def formatResult(diceValue:int) -> str:
        if (diceValue == 6):
            returnMessage = "+ " + str(diceValue) + "\n"
        else:
            returnMessage = "# " + str(diceValue) + "\n"
        return returnMessage

    @staticmethod
    def setDiceAsFear(diceValue:int) -> str:
        return "- " + str(diceValue) + "\n"

    @staticmethod
    def executeAction(diceQty:int, fearDice:int, bonusDice:int) -> str:
        try:
            diceCount = 0
            fearCount = 0
            returnMessage = "Result:\n"

            Dicer.validateDiceQty(diceQty)
            fearDice = Dicer.validateFearDice(fearDice)
            bonusDice = Dicer.validateBonusDice(bonusDice)

            while (diceCount < diceQty):
                diceValue = Dicer.throwDice(bonusDice)

                if (fearCount < fearDice):
                    returnMessage = returnMessage + Dicer.setDiceAsFear(diceValue)
                    fearCount += 1
                else:
                    returnMessage = returnMessage + Dicer.formatResult(diceValue)

                diceCount += 1

            return returnMessage
        except Exception  as error:
            Dicer.logger.info(error)
            raise error
