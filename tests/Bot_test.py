import os, re

from src.DiscordBot import DiscordBot

class TestBot():
    os.environ["DISCORD_TOKEN"] = 'TOKEN' 
    
    def test_SetBotToken(self):                
        discordBot = DiscordBot()
        assert discordBot.DISCORD_TOKEN == 'TOKEN'

    def test_AutoSetBotPrefix(self):        
        os.unsetenv("TEXT_PREFIX")
        discordBot = DiscordBot()
        assert discordBot.TEXT_PREFIX == '!sd-'

    def test_PassBotPrefix(self):        
        os.environ["TEXT_PREFIX"] = '!'
        discordBot = DiscordBot()
        assert discordBot.TEXT_PREFIX == '!'

    def test_InvalidDiceThrowed(self):
        discordBot = DiscordBot()
        diceQty = 0
        bonusDice = 0
        fearDice = 0
        assert '# Invalid dice quantity' in discordBot.throwDices(diceQty,fearDice,bonusDice) 

    def test_InvalidBonusThrowed(self):
        discordBot = DiscordBot()
        diceQty = 1
        bonusDice = 3
        fearDice = 0
        assert '# Invalid bonus value' in discordBot.throwDices(diceQty,fearDice,bonusDice)

    def test_MinimumFearThrowed(self):
        discordBot = DiscordBot()
        diceQty = 1
        bonusDice = 0
        fearDice = 0
        assert re.search(r"- [1-6]",discordBot.throwDices(diceQty,fearDice,bonusDice))

    def test_ThrowFiveDices(self):
        discordBot = DiscordBot()
        diceQty = 5
        bonusDice = 0
        fearDice = 0

        result = discordBot.throwDices(diceQty,fearDice,bonusDice)
        assert result.count('\n') == 6
