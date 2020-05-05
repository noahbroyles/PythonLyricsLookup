import requests
from bs4 import BeautifulSoup


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
    print(googleURL)
    response = requests.get(googleURL)
    soup = BeautifulSoup(response.text, 'html.parser')
    title = soup.find('span', class_="BNeawe tAd8D AP7Wnd").get_text()
    artist = soup.find_all('span', class_="BNeawe s3v9rd AP7Wnd")[-1].get_text()
    lyrics = soup.find_all('div', class_="BNeawe tAd8D AP7Wnd")[-1].get_text()
    return title, artist, lyrics

if __name__ == '__main__':
    song = input("What song are you looking for lyrics too? ")
    title, artist, lyrics = getLyrics(song)
    print("LYRICS TO {} BY {}:".format(title, artist))
    print("\n{}".format(lyrics))