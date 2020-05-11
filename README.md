# Spotify-to-csv
A python script powered by the spotipy library, as well as discogs API, to take a spotify playlist and return a csv of song by song info


### SETUP
- Download and install latest release of python 2.7
- Download and install pip (python package manager)
- Run commands pip install discogs-client & pip install spotipy

### USAGE
- run command python playlist_to_csv.py <SPOTIFY URI> <y or n for labels>
- Program will prompt for a name for a csv file
- Open csv with excel and fill out any missing info

### NOTES
- to get a spotify playlist URI click the 3 dots on its page and hover over "Share"
- commands may differ slightly depending on Mac/PC
- Unfortunately, discogs (service being used for label information) rate limiting may not like multiple people running this at the same time and cause the program to crash
