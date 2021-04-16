import re, os
import pytest
from src.main import SdBot

class TestSdBot():    
    sdBot = SdBot()

    def test_InvalidToken(self):
        with pytest.raises(Exception) as excinfo:   
            os.unsetenv("DISCORD_TOKEN")
            self.sdBot.startBot()                
            assert self.sdBot.errorHandleMessages[1000] in str(excinfo.value)

    def test_ValidToken(self):
        with pytest.raises(Exception) as excinfo:    
            os.environ["DISCORD_TOKEN"] = 'TOKEN'
            self.sdBot.startBot()    
            assert self.sdBot.errorHandleMessages[1003] in str(excinfo.value)
