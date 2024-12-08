
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

![Ping command](https://cdn.discordapp.com/attachments/1063539631058079776/1313288595087298591/image.png?ex=674f96d0&is=674e4550&hm=a3d21fa300116a2964d914af1994346ad05daf66c94e5e4aa9395b19001d8e47&)

> /balance

Check the amount of chips in your bank, starting balance is 100 chips

![Balance command](https://cdn.discordapp.com/attachments/1063539631058079776/1313289613896585216/image.png?ex=674f97c3&is=674e4643&hm=d811d45279faff9c2346529dbe1271309c97dfbeecfa9faf6d35ca6e12aa4319&)

> /daily

Gain 10 chips per day with this command

![Daily command](https://cdn.discordapp.com/attachments/1063539631058079776/1313289996144349244/image.png?ex=674f981e&is=674e469e&hm=92aea03b2f39ecf8c8ce090d5df197de398a75c79052d2f94415f0d3d0d1d442&)

> /challenge _user [wager]_

Challenge other users to 2 player games! You are able to wager 0 or more chips. Currently only Rock Paper Scissors is implemented.

![Challenge command](https://cdn.discordapp.com/attachments/1063539631058079776/1313338988932632627/image.png?ex=674fc5bf&is=674e743f&hm=2ea0d9ddcb102e7e16cd1b7be306be9a7bd85a485140d7e03689779e584070da&)

<br>

## Games

### Rock Paper Scissors
Classic dueling between 2 players!

![Rock Paper Scissors](https://cdn.discordapp.com/attachments/1063539631058079776/1313339710386737232/image.png?ex=674fc66b&is=674e74eb&hm=880b3ce54b4c3d33c0d9ac4175173a98be3067e1b678b00efe4c81f773016c30&)
![RPS Winner](https://cdn.discordapp.com/attachments/1063539631058079776/1313339818209443840/image.png?ex=674fc685&is=674e7505&hm=b0484de0f1d47959205428166f7dcff941fc6fa2f720926aab3f495641639141&)


### Blackjack
> /blackjack _wager_

Complete single player blackjack in discord, along with a custom table and clean design!

![Blackjack](https://cdn.discordapp.com/attachments/1063539631058079776/1313340743313526814/image.png?ex=674fc761&is=674e75e1&hm=4b9c4767165feb7fa85547759073cc1e4ab712481193353ed8dd3beddd16ddb5&)
![Blackjack2](https://cdn.discordapp.com/attachments/1063539631058079776/1313341081026297877/image.png?ex=674fc7b2&is=674e7632&hm=4d7cf049c04fdb20c28dbc5f232e33e568f4a1c9b59355528d5b515745c85651&)


### Roulette
> /roulette _wager_

Single player roulette with (nearly) every betting option! Custom UI not integrated.

![Roulette](https://cdn.discordapp.com/attachments/1063539631058079776/1315446531700297779/image.png?ex=6757708c&is=67561f0c&hm=56eeb8817dfdf4454ebaaae669275e9a792353d284ad4443c7c432660fcaa4ff&)
![RouletteDropdown](https://cdn.discordapp.com/attachments/1063539631058079776/1315446621823307806/image.png?ex=675770a2&is=67561f22&hm=25375a1d7dcab7ffbfbc8a00205cef6232ab7b799fb3f345b1baff90d2c9a7b7&)
![RouletteNumberSelect](https://cdn.discordapp.com/attachments/1063539631058079776/1315447031590031500/image.png?ex=67577104&is=67561f84&hm=a2f6b9c55e7cb458b48a4165bd61aa2f23654b61fcbc50d6f7c4bf924c5501a6&)
![RouletteWin](https://cdn.discordapp.com/attachments/1063539631058079776/1315447123990286336/image.png?ex=6757711a&is=67561f9a&hm=6005b5d5a15cb8310690a183deb75e034aa33758fa7e50918ed4df6377eb6f64&)

<br>

## Checklist/Roadmap
- [x] Discord bot design
- [X] API and Database
- [X] Interaction commands
- [X] Ping and basic features
- [X] Challenge module
- [X] Daily Login and Balance
- [X] Rock Paper Scissors
- [X] Blackjack
- [ ] Roulette
- [ ] Poker
- [ ] Profile Viewer
- [ ] Server Rewards
- [ ] Leaderboards
