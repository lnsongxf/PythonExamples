__author__ = 'tirthankar'
import twitter

# what is trending on Twitter
trending = twitter.Twitter()
results = trending.trends._woeid(_woeid = 1)

trends = trending.trends._woeid()
print([trend["name"] for trend in trending["trends"]])