import spotipy
from spotipy.oauth2 import SpotifyOAuth
import time
import pandas as pd



# Replace with your own credentials and redirect URI
client_id = '54ba602bcaab4e1b95ee13a083fa9f11'
client_secret = '3e04959b58d645e0bfa03c834de306b8'
redirect_uri = 'https://example.com'

# scope = "user-library-modify"
scope = 'user-library-read user-read-recently-played user-library-modify'

username = "12134759581"

def test():

    auth_manager=SpotifyOAuth(
            client_id=client_id,
            client_secret=client_secret,
            redirect_uri=redirect_uri,
            scope=scope)

    sp = spotipy.Spotify(auth_manager=auth_manager)

    # recently_played_tracks = sp.current_user_recently_played()
    #
    # # Print the recently played tracks


    # Calculate the timestamp for 90 days ago (in milliseconds)

    ninety_days_ago = int((time.time() - 90 * 24 * 60 * 60) * 1000)

    # Fetch the user's recently played tracks over the last 90 days
    tracks = []
    before = None

    while True:
        recently_played = sp.current_user_recently_played(limit=50, before=before)

        if not recently_played['items']:
            break

        for item in recently_played['items']:
            played_at = int(time.mktime(time.strptime(item['played_at'], "%Y-%m-%dT%H:%M:%S.%fZ")) * 1000)

            if played_at < ninety_days_ago:
                break

            tracks.append(item)

        before = played_at

    df = pd.DataFrame()
    for idx, item in enumerate(tracks, start=1):
        track = item['track']
        played_at = item['played_at']
        print(f"{idx} {track['name']} by {track['artists'][0]['name']} (Played at: {played_at})")

