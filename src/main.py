from DiscordBot import DiscordBot

class SdBot:
    # DEFAULT CONSTANT VALUES
    errorHandleMessages = {
    }

    def startBot(self):        
        try:
            discordbot = DiscordBot()
            discordbot.startBot()
        except Exception as error:
            raise error

if __name__ == '__main__':
    try:
        sdBot = SdBot()
        sdBot.startBot()
    except Exception as error:
        raise error
