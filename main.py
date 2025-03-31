from youtube_music_api_client.youtube_music_api_client import YoutubeMusicApiClient
from twitch_song_request_client.twitch_client import TwitchClient

import asyncio

async def main():
    ytm_client = YoutubeMusicApiClient()
    ytm_client.authenticate()

    current_song = ytm_client.get_current_song()
    print(f"{current_song['artist']} - {current_song['title']}")

    twitch_client = TwitchClient()
    twitch_client.bind_get_current_song(ytm_client.get_current_song)
    twitch_client.bind_search_and_queue(ytm_client.search_and_queue)
    # TODO Bind other commands

    await twitch_client.run()

    # lets run till we press enter in the console
    try:
        input('Press ENTER to stop\n')
    finally:
        # now we can close the chat bot and the twitch api client
        await twitch_client.close()


if __name__ == "__main__":
    asyncio.run(main())
