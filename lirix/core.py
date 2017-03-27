# -*- coding: utf-8 -*-
from . import helpers
from . import services as s
from ebooklib import epub
from song import Song

services_list = [s._wikia, s._musixmatch, s._songmeanings, s._songlyrics, s._genius, s._versuri]
error = "Error: Could not find lyrics."

def load_lyrics(artist, song):
    for service in services_list:
        lyrics, url = service(artist, song)
        if lyrics != error:
            lyrics = lyrics.replace("&amp;", "&").replace("`", "'").strip()
            return Song(artist, song, lyrics)
        
    return Song(artist, song, "Could not find lyrics")

def write_epub(songs):
    

    book = epub.EpubBook()
    
    # set metadata
    book.set_identifier('id123456')
    book.set_title('Sample book')
    book.set_language('en')
    
    book.add_author('Author Authorowski')
    book.add_author('Danko Bananko', file_as='Gospodin Danko Bananko', role='ill', uid='coauthor')
    
    for song in songs:
    
        # create chapter
        c1 = epub.EpubHtml(title=song.artist, file_name='chap_01.xhtml', lang='en')
        c1.content=u'<h1>Intro heading</h1><p>Žaba je skočila u baru.</p>'
        
        # add chapter
        book.add_item(c1)
        
        # define Table Of Contents
        book.toc = (epub.Link('chap_01.xhtml', 'Introduction', 'intro'),
                    (epub.Section('Simple book'),
                     (c1, ))
        )
        
    # add default NCX and Nav file
    book.add_item(epub.EpubNcx())
    book.add_item(epub.EpubNav())
    
    # define CSS style
    style = 'BODY {color: white;}'
    nav_css = epub.EpubItem(uid="style_nav", file_name="style/nav.css", media_type="text/css", content=style)
    
    # add CSS file
    book.add_item(nav_css)
    
    # basic spine
    book.spine = ['nav', c1]
    
    # write to the file
    epub.write_epub('test.epub', book, {})


def hmm():
    """Contemplation..."""
    if helpers.get_answer():
        print(get_hmm())
