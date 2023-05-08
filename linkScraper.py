from gnews import GNews

google_news = GNews(language = 'en')

# get top news stories, in the future consider more specificity

top = google_news.get_top_news()

# empty list to hold the top 3 urls of the day
urls = []

# append the top 3 urls to the list, this number can be adjusted 
for url in top[0:3]:

    urls.append(url['url'])
