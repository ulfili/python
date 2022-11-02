"""Twitter."""
from operator import attrgetter
import re

class Tweet:
    """Tweet class."""

    def __init__(self, user: str, content: str, time: float, retweets: int):
        """
        Tweet constructor.

        :param user: Author of the tweet.
        :param content: Content of the tweet.
        :param time: Age of the tweet.
        :param retweets: Amount of retweets.
        """
        self.user = user
        self.content = content
        self.time = time
        self.retweets = retweets


class Popularity:
    def __init__(self, hashtag, retweets):
        self.hashtag = hashtag
        self.retweets = retweets

    def __repr__(self):
        return '{' + self.hashtag + ', ' + str(self.retweets) + '}'


def find_fastest_growing(tweets: list) -> Tweet:
    """
    Find the fastest growing tweet.

    A tweet is the faster growing tweet if its "retweets/time" is bigger than the other's.
    >Tweet1 is 32.5 hours old and has 64 retweets.
    >Tweet2 is 3.12 hours old and has 30 retweets.
    >64/32.5 is smaller than 30/3.12 -> tweet2 is the faster growing tweet.

    :param tweets: Input list of tweets.
    :return: Fastest growing tweet.
    """
    index = 0
    tweet_num = 0
    tweet_growing = tweets[0].retweets / tweets[0].time      # võrdlen esimest tweeti tesitega
    for tweet in tweets:
        speed = tweet.retweets / tweet.time
        # print("speed is: ", speed, "index is: ", index)
        if speed < tweet_growing:
            # print("growing ", tweet_growing,  "is less than current speed ", speed)
            tweet_growing = speed
            tweet_num = index
            # print("fastest growing tweet index is: ", tweet_num)
        index = index + 1
    return tweets[tweet_num]


def sort_by_popularity(tweets: list) -> list:
    """
    Sort tweets by popularity.

    Tweets must be sorted in descending order.
    A tweet is more popular than the other if it has more retweets.
    If the retweets are even, the newer tweet is the more popular one.
    >Tweet1 has 10 retweets.
    >Tweet2 has 30 retweets.
    >30 is bigger than 10 -> tweet2 is the more popular one.

    :param tweets: Input list of tweets.
    :return: List of tweets by popularity
    """
    returned_list = sorted(tweets, key=attrgetter("time"))
    returned_list_2 = sorted(returned_list, key=attrgetter("retweets"), reverse=True)
    return returned_list_2


def filter_by_hashtag(tweets: list, hashtag: str) -> list:
    """
    Filter tweets by hashtag.

    Return a list of all tweets that contain given hashtag.

    :param tweets: Input list of tweets.
    :param hashtag: Hashtag to filter by.
    :return: Filtered list of tweets.
    """
    given_hashtag_tweets = []
    pattern = r"#\w+"
    for tweet in tweets:
        hashtags_list_in_tweet = []
        for match in re.finditer(pattern, tweet.content):
            found_hashtag = match.group()
            hashtags_list_in_tweet.append(found_hashtag)
        # print("founded list of hashtags are: ", hashtags_list_in_tweet)
        if hashtag in hashtags_list_in_tweet:
            # print("hashtag present in tweet ", tweet.content)
            given_hashtag_tweets.append(tweet)
    return given_hashtag_tweets


def sort_hashtags_by_popularity(tweets: list) -> list:
    """
    Sort hashtags by popularity.

    Hashtags must be sorted in descending order.
    A hashtag's popularity is the sum of its tweets' retweets.
    If two hashtags are equally popular, sort by alphabet from A-Z to a-z (upper case before lower case).
    >Tweet1 has 21 retweets and has common hashtag.
    >Tweet2 has 19 retweets and has common hashtag.
    >The popularity of that hashtag is 19 + 21 = 40.

    :param tweets: Input list of tweets.
    :return: List of hashtags by popularity.
    """
    hashtag_popularity = {}
    pattern = r"#\w+"
    for tweet in tweets:
        hashtags_list_in_tweet = []
        for match in re.finditer(pattern, tweet.content):
            found_hashtag = match.group()
            hashtags_list_in_tweet.append(found_hashtag)
        for hashtag in hashtags_list_in_tweet:
            if hashtag in hashtag_popularity:
                hashtag_popularity[hashtag] = hashtag_popularity.get(hashtag) + tweet.retweets
            else:
                hashtag_popularity[hashtag] = tweet.retweets
        print(hashtag_popularity)
    tag_pop_list = []
    for key, value in hashtag_popularity.items():
        tag_pop = Popularity(key, value)
        tag_pop_list.append(tag_pop)
    # print(tag_pop_list)
    tag_pop_list.sort(key=attrgetter("hashtag"))
    tag_pop_list.sort(key=attrgetter("retweets"), reverse=True)
    print("hashtags list", tag_pop_list)
    return_hashtags_list = []
    for tag in tag_pop_list:
        return_hashtags_list.append(tag.hashtag)
    print(return_hashtags_list)
    return return_hashtags_list


if __name__ == '__main__':
    tweet1 = Tweet("@realDonaldTrump", "Despite the negative press covfefe #bigsmart", 1249, 54303)
    tweet2 = Tweet("@elonmusk", "Technically, alcohol is a solution #bigsmart", 366.4, 166500)
    tweet3 = Tweet("@CIA", "We can neither confirm nor deny that this is our first tweet. #heart", 2192, 284200)
    tweet4 = Tweet("@messi", "Test #test #football #life", 6466, 54303 )
    tweets = [tweet1, tweet2, tweet3, tweet4]

    # print(find_fastest_growing(tweets).user)  # -> "@elonmusk"

   # filtered_by_popularity = sort_by_popularity(tweets)
   # for tw in filtered_by_popularity:
       # print(tw.user, tw.retweets, tw.time)
    # print(filtered_by_popularity[0].user)  # -> "@CIA"
    # print(filtered_by_popularity[1].user)  # -> "@elonmusk"
    # print(filtered_by_popularity[2].user)  # -> "@realDonaldTrump"


    # filtered_by_hashtag = filter_by_hashtag(tweets, "#life")
    # for tw in filtered_by_hashtag:
    #    print(tw.content)
    # print(filtered_by_hashtag[0].user)  # -> "@realDonaldTrump"
    # print(filtered_by_hashtag[1].user)  # -> "@elonMusk"

    sorted_hashtags = sort_hashtags_by_popularity(tweets)
    for tag in sorted_hashtags:
        print(tag)
    print(sorted_hashtags[0])  # -> "#heart"
