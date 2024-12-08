
# Aw Dangit Bot
Let's go gambling!

### Installation
Requires these additional python libraries:
- discord.py
- easy-pil
- fastapi
- pydantic
- python-dotenv
- requests
- sqlalchemy
- uvicorn

1. Create a .env file with a variable called DISCORD_BOT_TOKEN with your bot's token
2. Start the API using the file RUN_API.bat
3. Start the Bot using the file RUN_BOT.bat

## Features
> /ping

Straight forward command that gives the latency of the bot

![Ping command](https://github.com/user-attachments/assets/0b4a746c-803c-4a95-af91-53142f16c335)

> /balance

Check the amount of chips in your bank, starting balance is 100 chips

![Balance Command](https://github.com/user-attachments/assets/7520f3d8-bdfe-4118-bb3c-2c65d698bf09)

> /daily

Gain 10 chips per day with this command

![Daily Command](https://github.com/user-attachments/assets/a4c65391-5791-4e8c-9234-02f3674368da)

> /challenge _user [wager]_

Challenge other users to 2 player games! You are able to wager 0 or more chips. Currently only Rock Paper Scissors is implemented.

![Challenge Command](https://github.com/user-attachments/assets/b5363f55-43ed-4a2b-b747-64a8318bc34d)

<br>

## Games

### Rock Paper Scissors
Classic dueling between 2 players!

![Rock Paper Scissors](https://github.com/user-attachments/assets/0822a553-99ca-47f9-ada7-28470978bf73)
![RPS Winner](https://github.com/user-attachments/assets/3c10bb3e-7dca-4c31-b7db-9ba5383ca8d7)


### Blackjack
> /blackjack _wager_

Complete single player blackjack in discord, along with a custom table and clean design!

![Blackjack](https://github.com/user-attachments/assets/21b3cb42-44c1-4902-a34d-9be6aa5d4945)
![Blackjack2](https://github.com/user-attachments/assets/d5c3d467-f898-4d84-a9da-a2a65ea74ecd)


### Roulette
> /roulette _wager_

Single player roulette with (nearly) every betting option! Custom UI not integrated.

![Roulette](https://github.com/user-attachments/assets/0f8c4d1d-c81f-4525-9758-9c209d4c8cca)
![RouletteDropdown](https://github.com/user-attachments/assets/9ac01e55-a37f-4eef-bc05-00d255010e46)
![RouletteNumberSelect](https://github.com/user-attachments/assets/35852977-8153-45a9-8894-357a4927b072)
![RouletteWin](https://github.com/user-attachments/assets/f5ad1417-7fff-4e9b-a685-cb3f49803d5c)

<br>

## Checklist/Roadmap
- :white_check_mark: Discord bot design
- :white_check_mark: API and Database
- :white_check_mark: Interaction commands
- :white_check_mark: Ping and basic features
- :white_check_mark: Challenge module
- :white_check_mark: Daily Login and Balance
- :white_check_mark: Rock Paper Scissors
- :white_check_mark: Blackjack
- :white_check_mark: Roulette
- :x: Poker
- :x: Profile Viewer
- :x: Server Rewards
- :x: Leaderboards
