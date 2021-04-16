import os, pytest

from src.DiscordBot import DiscordBot

class TestBot():
    os.environ["DISCORD_TOKEN"] = 'TOKEN' 
    
    def test_AutoSetBotPrefix(self):        
        os.unsetenv("TEXT_PREFIX")
        discordBot = DiscordBot()
        assert discordBot.TEXT_PREFIX == '!sd-'

    def test_PassBotPrefix(self):        
        os.environ["TEXT_PREFIX"] = '!'
        discordBot = DiscordBot()
        assert discordBot.TEXT_PREFIX == '!'

    def test_SetBotToken(self):                
        discordBot = DiscordBot()
        discordBot.setDiscordToken()
        assert discordBot.DISCORD_TOKEN == 'TOKEN'

    def test_EmptyBotToken(self):                
        os.unsetenv("DISCORD_TOKEN")
        discordBot = DiscordBot()
        discordBot.setDiscordToken()
        assert discordBot.DISCORD_TOKEN == 'TOKEN'

    def test_StartInvalidToken(self):
        with pytest.raises(Exception) as excinfo:   
            discordBot = DiscordBot()
            discordBot.DISCORD_TOKEN = ""
            discordBot.startBot()                
            assert self.sdBot.errorHandleMessages[1000] in str(excinfo.value)

    def test_StartValidToken(self):
        with pytest.raises(Exception) as excinfo:    
            os.environ["DISCORD_TOKEN"] = 'TOKEN'
            discordBot = DiscordBot()            
            discordBot.startBot()
            assert self.sdBot.errorHandleMessages[1003] in str(excinfo.value)