import os

import pytest

from sd_bot.sd_bot import DiscordBot


class TestBot:
    os.environ["DISCORD_TOKEN"] = "TOKEN"

    def test_auto_set_bot_prefix(self):
        os.unsetenv("TEXT_PREFIX")
        discord_bot = DiscordBot()
        assert discord_bot.TEXT_PREFIX == "!sd-"

    def test_pass_bot_prefix(self):
        os.environ["TEXT_PREFIX"] = "!"
        discord_bot = DiscordBot()
        assert discord_bot.TEXT_PREFIX == "!"

    def test_set_bot_token(self):
        discord_bot = DiscordBot()
        discord_bot.set_discord_token()
        assert discord_bot.DISCORD_TOKEN == "TOKEN"

    def test_empty_bot_token(self):
        os.unsetenv("DISCORD_TOKEN")
        discord_bot = DiscordBot()
        discord_bot.set_discord_token()
        assert discord_bot.DISCORD_TOKEN == "TOKEN"

    def test_start_invalid_token(self):
        with pytest.raises(Exception) as excinfo:
            discord_bot = DiscordBot()
            discord_bot.DISCORD_TOKEN = ""
            discord_bot.start_bot()
        assert discord_bot.ERROR_HANDLE_MESSAGES[1000] in str(excinfo.value)

    def test_start_valid_token(self):
        with pytest.raises(Exception) as excinfo:
            os.environ["DISCORD_TOKEN"] = "TOKEN"
            discord_bot = DiscordBot()
            discord_bot.start_bot()
        assert discord_bot.ERROR_HANDLE_MESSAGES[1002] in str(excinfo.value)
