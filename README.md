# botDiscord
This project consists in a custom discord bot that has the objective of reading inputs from a discord server, presenting information based on the inputs given.
It's primary use is to read reviews of music albums, present that review to the rest of the server in a formatted manner and register that review in a Google Sheets spreadsheet to further down the line provide statistics trought other server inputs.

## Dependencies
[Nextcord](https://docs.nextcord.dev/en/stable/)

[Asyncio](https://docs.python.org/3/library/asyncio.html)

[Google-API-Python-Client](https://github.com/googleapis/google-api-python-client)

[Thinker-Desginer](https://github.com/ParthJadhav/Tkinter-Designer)

## Getting Started
After downloading the repository you'll need to create a *config.py* in the same directory and add the following lines according to your API Keys.
```
TOKEN = "Your Discord Bot Token"

GOOGLESEARCHAPI = "Your google search API Key"

CX = "Your Custom Search Engine Key"

SERVERID = Your Discord Server ID"
```


## Usage
### Review Command
/review [artist name] [album artist] [review] [veredict]
