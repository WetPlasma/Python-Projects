from bs4 import BeautifulSoup
import requests
from pprint import pprint
import re
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Spotify API credentials
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id="e",
    client_secret="e",
    redirect_uri="example.com",
    scope="playlist-modify-public"
))

# Test authentication
user = sp.current_user()
print(f"Authenticated as: {user['display_name']}")




date=input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD:")
print(date)
response = requests.get("https://www.billboard.com/charts/hot-100/" + date)

site_data=BeautifulSoup(response.text, "html.parser")   

list_with_h3=site_data.find_all(name="li", class_="lrv-u-width-100p")
# print(list_with_h3 )

titles=[]
for i in list_with_h3:
    
    title=i.find(name="h3")#.strip(True)
    if title:
        title=title.get_text(strip=True)
        print(title)
        titles.append(title)
    else:
        continue


print(titles)

track_uris = []

try:
    user_id = sp.current_user()["id"]  # Get the user's Spotify ID
    playlist_name = "My New Playlist"  # Customize the playlist name
    playlist_description = "A description of my new playlist."  # Customize the description

    # Create the playlist (private or public)
    new_playlist = sp.user_playlist_create(user=user_id, name=playlist_name, public=True, description=playlist_description)
    
    new_playlist_id = new_playlist["id"]  # Get the ID of the new playlist
    print(f"Created new playlist: {playlist_name} (ID: {new_playlist_id})")
except Exception as e:
    print(f"Error creating playlist: {e}")




for title in titles:
    try:
        results = sp.search(q=title, type="track", limit=1)
        tracks = results.get("tracks", {}).get("items", [])
        if tracks:
            track_uri = tracks[0]["uri"]
            track_uris.append(track_uri)
    except Exception as e:
        print(f"Error searching for track '{title}': {e}")


print(f"Found {len(track_uris)} tracks on Spotify.")

def validate_spotify_uris(uris):
    valid_uris = []
    for uri in uris:
        if re.match(r"^spotify:track:[a-zA-Z0-9]{22}$", uri):  # Spotify track URIs are 22-character Base62 strings
            valid_uris.append(uri)
        else:
            print(f"Invalid URI skipped: {uri}")
    return valid_uris


track_uris = validate_spotify_uris(track_uris)

print("Final track URIs:", track_uris)

if track_uris:
    try:
        sp.playlist_add_items(new_playlist_id, track_uris)
        print("Songs successfully added to your playlist!")
    except Exception as e:
        print(f"Error adding tracks to playlist: {e}")
else:
    print("No tracks were found. Please check your song titles or Spotify credentials.")
