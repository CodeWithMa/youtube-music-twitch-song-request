# YouTube Music Twitch Song Request

Application that uses the api exposed by [youtube-music](https://github.com/th-ch/youtube-music) to add song requests from twitch chat.

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
