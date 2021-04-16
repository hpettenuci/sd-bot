from DiscordBot import DiscordBot

class SdBot:
    # DEFAULT CONSTANT VALUES
    errorHandleMessages = {
    }

    def startBot(self):        
        discordbot = DiscordBot()
        discordbot.startBot()

if __name__ == '__main__':
    sdBot = SdBot()
    sdBot.startBot()
