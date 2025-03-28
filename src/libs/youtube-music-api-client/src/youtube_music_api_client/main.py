import requests

api_base_url = "http://localhost:26538/api/v1"

# post search
def search(query: str):
    url = f"{api_base_url}/search"
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjEiLCJpYXQiOjE3NDMxNjU2NTV9.NUMEud1m7Za4PMWo9XtdAc-iUEtP_nFTXRmxqbwVbMM",
        "Content-Type": "application/json",
    }
    data = {"query": query}

    response = requests.post(url, json=data, headers=headers)

    print("Status: ", response.status_code)

    # write to file
    #with open("search.json", "w") as f:
    #    f.write(response.text)

    contents = response.json()["contents"]["tabbedSearchResultsRenderer"]["tabs"][0]["tabRenderer"]["content"]["sectionListRenderer"]["contents"][1]
    if "musicCardShelfRenderer" in contents:
        first_search_result = contents["musicCardShelfRenderer"]["title"]["runs"][0]
        print(f"Adding first search result: {first_search_result['text']}")
        video_id = first_search_result['navigationEndpoint']['watchEndpoint']['videoId']
        print(f"Video ID: {video_id}")

        return video_id

    return None

def queue(video_id: str):
    url = f"{api_base_url}/queue"
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjEiLCJpYXQiOjE3NDMxNjU2NTV9.NUMEud1m7Za4PMWo9XtdAc-iUEtP_nFTXRmxqbwVbMM",
        "Content-Type": "application/json",
    }
    data = {"videoId": video_id, "insertPosition": "INSERT_AT_END"}

    response = requests.post(url, json=data, headers=headers)

    print("Status: ", response.status_code)
