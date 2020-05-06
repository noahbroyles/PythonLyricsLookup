import sys
from bs4 import BeautifulSoup
from requests_html import HTMLSession


def getLyrics(songSearch):
    percents = {" ": "+", "!": "%21", '"': "%22", "#": "%23", "$": "%24", "%": "%25", "&": "%26", "'": "%27", "(": "%28", ")": "%29", "*": "%2A", "+": "%2B", "`": "%60", ",": "%2C", "-": "%2D", ".": "%2E", "/": "%2F"}
    searchQuery = ""
    for char in songSearch:
        if char in percents.keys():
            char = percents[char]
        searchQuery += char
    if 'lyrics' not in searchQuery.lower():
        searchQuery += '+lyrics'
    googleURL = "https://google.com/search?q=" + searchQuery

    s = HTMLSession()
    response = s.get(googleURL)
    before = response.html.html
    response.html.render()
    after = response.html.html

    try:
        assert (before != after)
    except AssertionError:
        sys.exit("Rendering isn't happening. You're screwed.")

    soup = BeautifulSoup(response.html.html, 'html.parser')
    try:
        songTitle = soup.find('div', attrs={'data-attrid': 'title'}).get_text()
        songArtist = soup.find('div', attrs={'data-attrid': 'subtitle'}).get_text().replace(', ...', '')
        lyricDiv = [div for div in soup.find_all('div', attrs={'data-lyricid': True})][0]
        soup = BeautifulSoup(str(lyricDiv), 'html.parser')
        songLyrics = ''
        lyricDivs = soup.find_all('div')
        i = 0
        while i < len(lyricDivs):
            if '…' in lyricDivs[i].get_text():
                # Skip this and the next one
                i += 2
            else:
                for span in lyricDivs[i].findChildren('span'):
                    songLyrics += span.get_text() + "\n"
                songLyrics += "\n\n"
                i += 1
    except AttributeError:
        # This song ain't got lyrics on google
        sys.exit("No lyrics found")
    return songTitle, songArtist, songLyrics


if __name__ == '__main__':
    logo = """
    __               _               _______
   / /   __  _______(_)_________    / / ___/
  / /   / / / / ___/ / ___/ ___/_  / /\__ \ 
 / /___/ /_/ / /  / / /__(__  ) /_/ /___/ / 
/_____/\__, /_/  /_/\___/____/\____//____/  
      /____/                                            
    """
    print(logo)
    song = input("What song are you looking for lyrics to? ")
    title, artist, lyrics = getLyrics(song)
    print("{} by {}:".format(title, artist))
    print("\n" + lyrics)
