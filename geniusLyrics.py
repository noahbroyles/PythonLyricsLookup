import requests
from bs4 import BeautifulSoup
import sys
import re


def getLyrics(songSearch, withAnnotations=True):
    percents = {" ": "+", "!": "%21", '"': "%22", "#": "%23", "$": "%24", "%": "%25", "&": "%26", "'": "%27", "(": "%28", ")": "%29", "*": "%2A", "+": "%2B", "`": "%60", ",": "%2C", "-": "%2D", ".": "%2E", "/": "%2F"}
    searchQuery = ""
    for char in songSearch:
        if char in percents.keys():
            char = percents[char]
        searchQuery += char
    if 'lyrics' not in searchQuery.lower():
        searchQuery += '%20lyrics'
    searchURL = "https://google.com/search?q=" + searchQuery
    response = requests.get(searchURL)
    soup = BeautifulSoup(response.content, 'html.parser')

    try:
        goodLink = [link['href'] for link in soup.find_all('a') if 'genius.com' in link['href']][0].replace('/url?q=', '').split('&')[0]
    except IndexError:
        sys.exit("No lyrics found")

    lyricsPage = BeautifulSoup(requests.get(goodLink).content, 'html.parser')

    try:
        songTitle = lyricsPage.find('h1').get_text().strip("\n")
        songArtist = lyricsPage.find('h2').get_text().strip("\n")
        songLyrics = lyricsPage.find('div', class_="lyrics").get_text()
    except AttributeError:
        sys.exit("No lyrics found")

    if not withAnnotations:
        songLyrics = re.sub(r'\[.*?\]', '', songLyrics)

    return songTitle, songArtist, songLyrics

if __name__ == '__main__':
    logo = """
   ___          _           _            _       
  / __|___ _ _ (_)_  _ ___ | |  _  _ _ _(_)__ ___
 | (_ / -_) ' \| | || (_-< | |_| || | '_| / _(_-<
  \___\___|_||_|_|\_,_/__/ |____\_, |_| |_\__/__/
                                |__/             
    """
    print(logo)
    song = input("What song are you looking for lyrics too? ")
    withAnno = input("Do you want annotations in your lyrics? ").lower()
    title, artist, lyrics = getLyrics(song, withAnnotations=True if withAnno.startswith('y') or not withAnno else False)
    print("{} by {}:".format(title, artist))
    print("\n" + lyrics)
