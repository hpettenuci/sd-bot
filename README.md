![Build and Push to GCR](https://github.com/hpettenuci/sd-bot/workflows/Build%20and%20Push%20to%20GCR/badge.svg) [![Conventional Commits](https://img.shields.io/badge/Conventional%20Commits-1.0.0-blue.svg)](https://conventionalcommits.org)

# Shotgun Diaries Discord Bot

This is a Discord Bot to help masters and players on Shootgun Diaries RPG campaigns using Discord.

---

## Bot Features

- Roll Action Dices - !sd-resource <qty fear dice> <qty bonus>
- Roll Resource Dices - !sd-action <qty action dices> <qty fear dices> <qty bonus>

## Future Features

- Create Campaign
    - Link Discord User to Master
    - List of Players
    - Master Notes
- Store Character Information
    - Owner of Char - Discord User
    - Name
    - Type
    - Background
    - Fear Dices
    - Bonus Points
    - Diary Notes

# Environment Variables

- **DISCORD_TOKEN** (required) - Discord Bot token
- **TEXT_PREFIX** (optional) - Text prefix to recognize bot commands (Default: !sd-)

---

## Setup
```sh
# Install pipx if pipenv and cookiecutter are not installed
python3 -m pip install pipx

# Install pipenv using pipx
pipx install pipenv

# Install dependencies
pipx run pipenv install --dev

# Setup pre-commit and pre-push hooks
pipx run pipenv run pre-commit install -t pre-commit
pipx run pipenv run pre-commit install -t pre-push
```