from twitchAPI.twitch import Twitch
from twitchAPI.type import AuthScope, ChatEvent
from twitchAPI.chat import Chat, EventData, ChatCommand
from twitchAPI.oauth import UserAuthenticationStorageHelper
from dotenv import load_dotenv
import os


class TwitchClient():
    def __init__(self):
        self.chat = None
        self.twitch = None
        self.get_current_song = None
    
    def bind_get_current_song(self, callback):
        self.get_current_song = callback

    def bind_search_and_queue(self, callback):
        self.search_and_queue = callback

    async def run(self):
        load_dotenv()

        APP_ID = os.getenv("TWITCH_APP_ID")
        if APP_ID is None:
            raise Exception("Environment variable TWITCH_APP_ID is not set")

        APP_SECRET = os.getenv("TWITCH_SECRET")
        if APP_SECRET is None:
            raise Exception("Environment variable TWITCH_SECRET is not set")

        USER_SCOPE = [AuthScope.CHAT_READ, AuthScope.CHAT_EDIT]

        async def on_ready(ready_event: EventData):
            print('TWITCH: Bot is ready for work')
            TWITCH_CHANNEL = os.getenv("TWITCH_CHANNEL")
            if TWITCH_CHANNEL:
                print(f"Joining {TWITCH_CHANNEL}.")
                await ready_event.chat.join_room(TWITCH_CHANNEL)
            else:
                print('No channel specified, not joining any channels')

        async def get_current_song_command_handler(cmd: ChatCommand):
            if self.get_current_song is None:
                return

            current_song = self.get_current_song()
            await cmd.reply(f"{current_song['artist']} - {current_song['title']}")

        async def song_request_command_handler(cmd: ChatCommand):
            if self.search_and_queue is None:
                return

            print(f"Received song request: {cmd.parameter}")
            self.search_and_queue(cmd.parameter)
            # TODO Reply to the user with added song

        twitch = await Twitch(APP_ID, APP_SECRET)
        helper = UserAuthenticationStorageHelper(twitch, USER_SCOPE)
        await helper.bind()

        # create chat instance
        chat = await Chat(twitch)

        # also save twitch and chat to class properties so we can shut them down
        # TODO Test if this is necessary
        self.twitch = twitch
        self.chat = chat

        # listen to when the bot is done starting up and ready to join channels
        chat.register_event(ChatEvent.READY, on_ready)

        # Directly register commands and their handlers
        chat.register_command('snow', get_current_song_command_handler)
        chat.register_command('sr', song_request_command_handler)
        # TODO Register commands for song requests

        chat.start()


    async def close(self):
        self.chat.stop()
        await self.twitch.close()
