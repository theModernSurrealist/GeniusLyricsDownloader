from lyricsgenius import Genius
from colorama import Fore, Back, Style
import os

os.system("title " + "Genius Lyrics Downloader")
genius = Genius("_9-AdC98aHf4jMbjqqYWUlbdGQWusroxqF3PPnOL0QMcSMqxmf_olbJUcC7-JXEC")
print(Fore.YELLOW + '''   ____            _             _               _            ____                      _                 _           
  / ___| ___ _ __ (_)_   _ ___  | |   _   _ _ __(_) ___ ___  |  _ \  _____      ___ __ | | ___   __ _  __| | ___ _ __ 
 | |  _ / _ \ '_ \| | | | / __| | |  | | | | '__| |/ __/ __| | | | |/ _ \ \ /\ / / '_ \| |/ _ \ / _` |/ _` |/ _ \ '__|
 | |_| |  __/ | | | | |_| \__ \ | |__| |_| | |  | | (__\__ \ | |_| | (_) \ V  V /| | | | | (_) | (_| | (_| |  __/ |   
  \____|\___|_| |_|_|\__,_|___/ |_____\__, |_|  |_|\___|___/ |____/ \___/ \_/\_/ |_| |_|_|\___/ \__,_|\__,_|\___|_|   
                                      |___/                                                                           ''')
print(Style.RESET_ALL)
print("Welcome to the Genius Lyrics Downloader.\nThis script was made by Miko Radley. Enjoy!\n")
url_fuzzy = input("Do you want to use a Genius URL or fuzzy search?\nType 'url' or 'fuzzy' to choose: ")

def end():
	print("Thank you for using the Genius Lyrics Downloader.")
	os.remove("y.txt")
	input()

def FuzzySearch():
	songArtist = input("Who is the artist of the song? ")
	songName = input("What is the name of the song? ")
	#artist = genius.search_artist(songArtist, max_songs=6, sort="title")
	headers = input("Do you want headers (e.g. [Chorus]) in the lyrics? y/n: ")
	if headers == "y":
		genius.remove_section_headers = False
	else:
		genius.remove_section_headers = True
	song = genius.search_song(songName, songArtist)
	print(song.lyrics)
	saveQueryFuzzy = input("Do you want to save these lyrics? y/n: ")
	if saveQueryFuzzy == "y":
		saveQueryFuzzyName = input("What do you want to save the lyrics as? ")
		f = open(saveQueryFuzzy + ".txt", "x")
		f = open(saveQueryFuzzyName + ".txt", "w")
		f.write(song.lyrics)
		f.close()

	else:
		end()

def URLSearch():
	urlInput = input("What is the Genius URL of the song? - ")
	headers = input("Do you want headers (e.g. [Chorus]) in the lyrics? y/n: ")
	if headers == "y":
		genius.remove_section_headers = False
	else:
		genius.remove_section_headers = True
	print(genius.lyrics(song_url=urlInput))
	saveQueryURL = input("Do you want to save these lyrics? y/n: ")
	if saveQueryURL == "y":
		saveQueryURLName = input("What do you want to save the lyrics as? ")
		f = open(saveQueryURLName + ".txt", "x")
		f = open(saveQueryURLName + ".txt", "w")
		f.write(genius.lyrics(song_url=urlInput))
		f.close()

	else:
		end()

if url_fuzzy == "fuzzy":
	FuzzySearch()

if url_fuzzy == "url":
	URLSearch()

end()