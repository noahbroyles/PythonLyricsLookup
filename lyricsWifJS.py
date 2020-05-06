from bs4 import BeautifulSoup
from requests_html import HTMLSession


def getLyrics(songSearch):
    percents = {" ": "%20", "!": "%21", '"': "%22", "#": "%23", "$": "%24", "%": "%25", "&": "%26", "'": "%27", "(": "%28", ")": "%29", "*": "%2A", "+": "%2B", "`": "%60", ",": "%2C", "-": "%2D", ".": "%2E", "/": "%2F"}
    searchQuery = ""
    for char in songSearch:
        if char in percents.keys():
            char = percents[char]
        searchQuery += char
    if 'lyrics' not in searchQuery.lower():
        searchQuery += '%20lyrics'
    googleURL = "https://google.com/search?q=" + searchQuery

    s = HTMLSession()
    response = s.get(googleURL)
    response.html.render()

    soup = BeautifulSoup(response.content, 'html.parser')
    title = soup.find('div', attrs={'data-attrid': 'title'}).get_text()
    artist = soup.find('div', attrs={'data-attrid': 'subtitle'}).get_text()
    lyrics = [div.get_text() for div in soup.find_all('div', attrs={'data-lyricid': 'Lyricfind002-1637413'})]
    print(soup.prettify())
    return title, artist, lyrics


if __name__ == '__main__':
    logo = """
    __               _          
   / /   __  _______(_)_________
  / /   / / / / ___/ / ___/ ___/
 / /___/ /_/ / /  / / /__(__  ) 
/_____/\__, /_/  /_/\___/____/  
      /____/                    
    """

    print(logo)
    song = input("What song are you looking for lyrics to? ")
    title, artist, lyrics = getLyrics(song)
    print("{} by {}:".format(title, artist))
    # print("\n" + lyrics)
