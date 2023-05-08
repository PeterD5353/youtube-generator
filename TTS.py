from gtts import gTTS

from summarizer import *
from linkScraper import * 

language = 'en'
counter = 0

for summary in summaries:

    counter +=1 
    text = summary

    speech = gTTS(text=text, lang=language, slow=False, tld = 'com.au')

    speech.save(f'tts{counter}.mp3')