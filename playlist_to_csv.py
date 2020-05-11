import sys
import os
import csv
import time

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

import discogs_client

os.environ['SPOTIPY_CLIENT_ID'] = "c12ac83979844635937cd1995b2aa452"
os.environ['SPOTIPY_CLIENT_SECRET'] = "2fec44949e00479eab83f13d8ba9c777"

client_credentials_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

tracks = sp.playlist_tracks(sys.argv[1], fields='items(track(track_number,name,artists,album(name)))')['items']

d = discogs_client.Client('Playlist to csv', user_token='sRIGFRtKHCuULPGWnLkOTNBwfHtKPGmcMIiJMyzU')

name = raw_input("Enter a name for this spreadsheet: ")

if sys.argv[2] is 'y':
	with open(name+'.csv', 'w') as csvfile:
		writer = csv.writer(csvfile, lineterminator='\n')
		for track in tracks:
			time.sleep(1.2)
			results = d.search(type='release', release_title=track['track']['album']['name'], track=track['track']['name'])
			if results.pages > 0:
				try:
					writer.writerow([track['track']['name'], track['track']['album']['name'], track['track']['artists'][0]['name'], results[0].labels[0].name])
				except IndexError:
					print("Error occured on track "+track['track']['name']+", no label will be listed in csv")
					try:
						writer.writerow([track['track']['name'], track['track']['album']['name'], track['track']['artists'][0]['name']])
					except UnicodeEncodeError:
						print("Non ASCII character found, no row printed")
				except UnicodeEncodeError:
					print("Non ASCII character found, no row printed")
			else:
				writer.writerow([track['track']['name'], track['track']['album']['name'], track['track']['artists'][0]['name'], "label not found"])
	csvfile.close()
else:
	with open(name+'.csv', 'w') as csvfile:
		writer = csv.writer(csvfile, lineterminator='\n')
		for track in tracks:
			try:
				writer.writerow([track['track']['name'], track['track']['album']['name'], track['track']['artists'][0]['name']])
			except UnicodeEncodeError:
				print("Non ASCII character found, no row printed")
	csvfile.close()