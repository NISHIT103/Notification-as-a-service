import requests

class task:
    def creation_task():
        url = "https://spotify.com"
        params = {
            "song_id": 12132,
            "song_name": "askdnak"
        }
        requests.post(url,params, headers)

    
