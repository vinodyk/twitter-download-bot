import tweepy
from secrets import *

auth = tweepy.OAuthHandler(API_KEY, API_SCRET)
auth.set_access_token(ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET)

#give time between tweets
api = tweepy.API(auth, wait_on_rate_limit = True)

def bot_begins():
	api.update_status("starting bot..")
	pass

def download_all_tweets(user):
	page_list = []

	for page in tweepy.Cursor(api.user_timeline, screen_name=user, tweet_mode ='extended').pages():
		page_list.append(page)

	with open ("bot_data.txt", "a", encoding="utf-8") as out_file:
		for page in page_list:
			for status in page:
				if not status.retweeted:
					#empty line to give a space between tweets
					out_file.write(status.full_text +"\n\n")
					print(status.full_text)

if __name__ == '__main__':
	#bot_begins()
	for user in ["user1","user2","user10"]:
		download_all_tweets(user)

