import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Replace with your own credentials and redirect URI
client_id = 'b8c3b2feccd34c74aa8948dbd696364b'
client_secret = 'dda19d29a3a343d08dfd51bf4fa1de48'
redirect_uri = 'https://example.com'

scope = "user-library-read"
username = "12134759581"

def test():
    auth_manager=SpotifyOAuth(
            client_id=client_id,
            client_secret=client_secret,
            redirect_uri=redirect_uri,
            scope=scope,
            username=username)
    # auth_url = auth_manager.get_authorize_url()
    # print(auth_url)
    # auth_manager.validate_token('AQAJ1-b4KlHUkHiiOK3xpb7xQwxNwb-nedkh0Ei-yXsy4F_VcNVgG5AeC1IHi8aiL8OR5UZ3sDTNqeFCkXCzTzNQoxIchg-ZmdZvIcOapsijqHqVCDcf6lBsAUeC4pt2ymocw6zqcAx8VaS3DilXxVWIpEA56LTW6LdPQ7Ly0XrTjOesyCaW5plQ')
    sp = spotipy.Spotify(auth_manager=auth_manager)
    # sp = spotipy.Spotify(
    #     auth_manager=SpotifyOAuth(
    #         client_id=client_id,
    #         client_secret=client_secret,
    #         redirect_uri=redirect_uri,
    #         scope=scope,
    #         username=username))

    results = sp.current_user_saved_tracks()
    for idx, item in enumerate(results['items']):
        track = item['track']
        print(idx, track['artists'][0]['name'], " – ", track['name'])