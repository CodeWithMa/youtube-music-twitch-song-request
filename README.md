# YouTube Music Twitch Song Request

Application that uses the api exposed by [youtube-music](https://github.com/pear-devs/pear-desktop) to add song requests from twitch chat.

## Configure

The following environment variables are required to connect to twitch chat.

- TWITCH_APP_ID
- TWITCH_SECRET

The channel variable is optional but the bot won't join any channels and won't listen to any requests :D

- TWITCH_CHANNEL

You can copy and edit the template [`.env.sample`](.env.sample) and rename it to `.env`.

Register an application in your [twitch dev dashboard](https://dev.twitch.tv/console). Add the following URL as a "OAuth Redirect URL": http://localhost:17563.

## Run

```bash
uv run main.py
```

## First start

### youtube-music

At the first start you will have to allow access to youtube-music-api.
A box will open which you have to allow.

After pressing Allow the connection fails.
For it to work you have to restart youtube-music.

### twitch api

The browser will open twitch and you can log in with the account you want the bot to use.
After logging in tokens will be saved in `user_token.json`.
