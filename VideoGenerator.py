import nltk
from newspaper import Article
from gnews import GNews
from gtts import gTTS
from mutagen.mp3 import MP3
from moviepy.editor import AudioFileClip, ImageClip, CompositeVideoClip, TextClip, VideoFileClip
from moviepy.video.tools.subtitles import SubtitlesClip
from bing_image_downloader import downloader

nltk.download('punkt')


# grab the top news article of the day

google_news = GNews(language = 'en')

top = google_news.get_top_news()

url = top[0]['url']

# parse the article to get a summary
article = Article(url)

sources = []

article.download()
article.parse()
article.nlp()

summary = article.summary
title = article.title

sources.append(url)
sources.append(title)

# generate and save tts
language = 'en'

speech = gTTS(text=summary, lang=language, slow=False, tld = 'com.au')

file = 'tts.mp3'

speech.save(file)

audio = MP3(file)

# download image relating to the article title 
downloader.download(title, limit=1, adult_filter_off=True, force_replace=False, timeout=60, verbose=False)

# define a fucntion to combine the audio and image 
def combine_photo_and_audio(image, audio):

  audio_clip = AudioFileClip(audio)

  image_clip = ImageClip(image)

  video_clip = image_clip.set_audio(audio_clip)

  video_clip.duration = audio_clip.duration

  video_clip.fps = 24

  video_clip.write_videofile("render.mp4")

# run the function on the audio and image 
combine_photo_and_audio(f'C:/Users/Peter/Desktop/projects/youtube-generator/dataset/{title}/Image_1.png', 'tts.mp3')

