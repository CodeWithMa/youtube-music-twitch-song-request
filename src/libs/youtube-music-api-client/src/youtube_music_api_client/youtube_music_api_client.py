import requests

class YoutubeMusicApiClient:
    def __init__(self):
        self.api_base_url = "http://localhost:26538"
        self.api_base_url_v1 = f"{self.api_base_url}/api/v1"
        self.token = ""

    def authenticate(self):
        # TODO Use real client id: youtube-music-twitch-song-request
        client_id = "1"
        url = f"{self.api_base_url}/auth/{client_id}"

        headers = {
            "accept": "application/json"
        }
        data = {}
        response = requests.post(url, json=data, headers=headers)

        print("Status: ", response.status_code)
        #print(response.json())

        if response.status_code != 200:
            return

        accessToken = response.json()["accessToken"]
        self.token = accessToken


    def get_current_song(self):
        url = f"{self.api_base_url_v1}/song"
        headers = {
            "accept": "application/json",
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json",
        }

        response = requests.get(url, headers=headers)

        print("Status: ", response.status_code)

        if response.status_code != 200:
            return None

        return response.json()


    def search(self, query: str):
        url = f"{self.api_base_url_v1}/search"
        headers = {
            "accept": "application/json",
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json",
        }
        data = {"query": query}

        response = requests.post(url, json=data, headers=headers)

        print("Status: ", response.status_code)

        # write to file
        #with open("search.json", "w") as f:
        #    f.write(response.text)

        if response.status_code != 200:
            return None
            
        contents = response.json()["contents"]["tabbedSearchResultsRenderer"]["tabs"][0]["tabRenderer"]["content"]["sectionListRenderer"]["contents"][1]
        if "musicCardShelfRenderer" in contents:
            first_search_result = contents["musicCardShelfRenderer"]["title"]["runs"][0]
            print(f"Adding first search result: {first_search_result['text']}")
            video_id = first_search_result['navigationEndpoint']['watchEndpoint']['videoId']
            print(f"Video ID: {video_id}")

            return video_id

        return None

    def queue(self, video_id: str):
        url = f"{self.api_base_url_v1}/queue"
        headers = {
            "accept": "application/json",
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json",
        }
        data = {"videoId": video_id, "insertPosition": "INSERT_AT_END"}

        response = requests.post(url, json=data, headers=headers)

        print("Status: ", response.status_code)
