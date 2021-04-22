from sd_bot.sd_bot import DiscordBot

if __name__ == "__main__":
    discordbot = DiscordBot()
    if discordbot.DISCORD_TOKEN != "SMOKE":
        discordbot.startBot()
