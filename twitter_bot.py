#Twtter bot to pull Elon Musk's tweets

from snscrape.modules.twitter import TwitterSearchScraper
import pandas as pd





#Create empty dataFrame that will hold all the tweets
total_tweets = pd.DataFrame(columns = ['Date', 'Tweet'])


username = 'elonmusk'
start_date = '2022-07-25'
end_date = '2022-08-01'

search_query = TwitterSearchScraper(f'from:{username} since:{start_date} until:{end_date}')


for tweet in search_query.get_items():
    #For each tweet, create a dataframe of that tweet and concat it to the total_tweets DataFrame
    new_tweet = pd.DataFrame([[tweet.date, tweet.content]], columns = ['Date', 'Tweet'])
    total_tweets = pd.concat([total_tweets, new_tweet], ignore_index = True)



#Export total tweets as csv
total_tweets.to_csv('data/elons_tweets.csv')


