# imports
import nltk
from newspaper import Article
nltk.download('punkt')

url = ""

article = Article(url)

article.download()
article.parse()
article.nlp()

summary = article.summary