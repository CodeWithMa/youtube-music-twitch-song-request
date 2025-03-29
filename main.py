from youtube_music_api_client.youtube_music_api_client import YoutubeMusicApiClient


def main():
    client = YoutubeMusicApiClient()
    client.authenticate()

    current_song = client.get_current_song()
    print(f"{current_song['artist']} - {current_song['title']}")

    # video_id = client.search("Never gonna")
    # if video_id is None:
    #     return
    # client.queue(video_id)


if __name__ == "__main__":
    main()
