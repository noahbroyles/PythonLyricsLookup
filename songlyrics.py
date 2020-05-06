import requests
from bs4 import BeautifulSoup
import sys


def getLyrics(songSearch):
    percents = {" ": "%20", "!": "%21", '"': "%22", "#": "%23", "$": "%24", "%": "%25", "&": "%26", "'": "%27", "(": "%28", ")": "%29", "*": "%2A", "+": "%2B", "`": "%60", ",": "%2C", "-": "%2D", ".": "%2E", "/": "%2F"}
    searchQuery = ""
    for char in songSearch:
        if char in percents.keys():
            char = percents[char]
        searchQuery += char
    if 'lyrics' not in searchQuery.lower():
        searchQuery += '%20lyrics'
    searchURL = "http://www.songlyrics.com/index.php?section=search&searchW=" + searchQuery + "&submit=Search"
    response = requests.get(searchURL)
    soup = BeautifulSoup(response.content, 'html.parser')
    goodLink = soup.find_all('div', class_='serpresult')[0].findChildren('a')[0]['href']
    lyricsPage = BeautifulSoup(requests.get(goodLink).content, 'html.parser')
    lyrics = lyricsPage.find(attrs={'id': 'songLyricsDiv'}).get_text()
    return lyrics


if __name__ == '__main__':
    logo = """
 ___  ___  _  _  ___   _ __   _____ ___ ___ ___ 
/ __|/ _ \| \| |/ __| | |\ \ / / _ \_ _/ __/ __|
\__ \ (_) | .` | (_ | | |_\ V /|   /| | (__\__ \\
|___/\___/|_|\_|\___| |____|_| |_|_\___\___|___/
                                                                                              
    """
    print(logo)
    song = input("What song are you looking for lyrics too? ")
    lyrics = getLyrics(song)
    print("\n" + lyrics)

