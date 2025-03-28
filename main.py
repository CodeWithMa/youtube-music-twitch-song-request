from youtube_music_api_client.main import search, queue


def main():
    video_id = search("Never gonna")
    if video_id is None:
        return
    queue(video_id)


if __name__ == "__main__":
    main()
