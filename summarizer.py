# imports
import nltk
from newspaper import Article
nltk.download('punkt')

from linkScraper import *

summaries = []

for url in urls:
    link = url

    article = Article(link)

    article.download()
    article.parse()
    article.nlp()

    summaries.append(article.summary)