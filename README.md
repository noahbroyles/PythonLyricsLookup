# PythonLyricsLookup
*Look up the lyrics to a song in Python!*

With the code in this repo, you can look up the lyrics to any song! There are 4 different methods for scraping lyrics, in the 4 files `googleLyrics.py`, `googleLyricsJS.py`, `songlyrics.py`, and `geniusLyrics.py`.
## Lyric Getting Functions:
In all the functions below, `songSearch` is any string, the name of a song.
### In `googleLyrics.py` and `googleLyricsJS.py`:
```python
getLyrics(songSearch)
  ... return title, artist, lyrics
```
Three strings are returned, `title`, `artist`, and `lyrics`.
<br>
### In `songlyrics.py`:
```python
getLyrics(songSearch)
  ... return lyrics
```
One string is returned, `lyrics`.
<br>
### In `geniusLyrics.py`:
```python
getLyrics(songSearch, withAnnotations=True)
  ... return title, artist, lyrics
```
`withAnnotations` means that your lyrics will have Genius markings in them. Like this:
```
[Chorus]
Today, I don't feel like doing...

[Verse 1]
I'm gonna...

[Pre-Chorus]
Oh oh, yes I said it
I said it, I said it, 'cause I can

[Chorus]
Today, I don't feel like doing...

[Verse 2]
Tomorrow, I'll wake up...
```
Without annotations, the same lyrics would look like this:
```
Today, I don't feel like doing...

I'm gonna...

Oh oh, yes I said it
I said it, I said it, 'cause I can

Today, I don't feel like doing...

Tomorrow, I'll wake up...
```
## What each file does:
### `googleLyrics.py`:
This method of finding lyrics is the fastest. It scrapes right from a Google search page and relies on some random class names. This could eventually not work anymore, if Google decides to change their ugly class names.
### `googleLyricsJS.py`:
This method of finding lyrics renders Javascript in a Google page and uses better scraping methods than `googleLyrics.py`. The only downside is that it is slower than `googleLyrics.py` because it renders Javascript and has more dependencies. It uses the [Python `requests-HTML`](https://github.com/psf/requests-html/) package, which downloads Chromium in the background the first time you use it.
So it takes more disk space and really isn't worth all that. However, it's likely to work longer than `googleLyrics.py` will.
### `songlyrics.py`:
This method of finding lyrics uses [songlyrics.com](http://www.songlyrics.com/), which is a random lyric site I found that isn't even secure. This does _not_ give the artist and title for songs that you look up, only the lyrics. **IF** it finds the song at all, which is _certainly_ debatable.
### `genuisLyrics.py`:
Uses Google to find a link to the song lyrics on the famous [Genuis.com](https://genius.com/). This is probably the best way to get the song lyrics because Genius has all the songs.  
 
   
 