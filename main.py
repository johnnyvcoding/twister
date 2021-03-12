import tweepy
import json
from flask import Flask, render_template, jsonify, request
import secret




auth = tweepy.OAuthHandler(secret.consumer_key, secret.consumer_secret)
auth.set_access_token(secret.access_token, secret.access_secret)

api = tweepy.API(auth)
app = Flask(__name__)


# public_tweets = api.user_timeline(screen_name="clemmihai")
# for tweet in public_tweets:
#     tweet.favorite()

# for tweet in tweepy.Cursor(api.user_timeline, screen_name="clemmihai").items(2):
#     tweet.favorite()


def favorite_recent_tweets(user, quantity):
    for tweet in tweepy.Cursor(api.user_timeline, screen_name=user).items(quantity):
        tweet.favorite()


def ret_recent_tweets(user, quantity):
    for tweet in tweepy.Cursor(api.user_timeline, screen_name=user).items(quantity):
        tweet.retweet()

def get_recent(user):
        arr = []
        for tweet in tweepy.Cursor(api.user_timeline, screen_name=user).items(1):
            arr.append(tweet.text)
            print('this is the type of tweet ', type(tweet))
        return arr

def follow_user(user):
    api.create_friendship(user)

def fun_test ():
    for tweet in tweepy.Cursor(api.user_timeline, screen_name="WellPaidGeek").items(1):
        return tweet._json

@app.route('/')
def hello ():
    return jsonify(fun_test())



@app.route('/retweet/<name>')
def main (name):
    ret_recent_tweets(name, 20)


@app.route('/fav/<name>/<quantity>')
def ok(name, quantity):
    favorite_recent_tweets(name, quantity)


if __name__ == '__main__':
  app.run(debug=True, host="0.0.0.0", port="1338")

# favorite_recent_tweets('kingjames')
