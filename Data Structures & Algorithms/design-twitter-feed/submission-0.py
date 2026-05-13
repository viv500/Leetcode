from collections import defaultdict
class Twitter:

    def __init__(self):
        self.following = defaultdict(set)
        self.tweets = []

    def postTweet(self, userId: int, tweetId: int) -> None:
        tweets = self.tweets
        tweets.append([tweetId, userId])

    def getNewsFeed(self, userId: int) -> List[int]:
        tweets = self.tweets
        following_list = self.following[userId]
        output = []

        for tweet_id, tweeter_id in tweets[::-1]:
            if len(output) == 10: break

            if tweeter_id in following_list or tweeter_id == userId:
                output.append(tweet_id)

        
        return output
    

    def follow(self, followerId: int, followeeId: int) -> None:
        following_list = self.following[followerId]
        following_list.add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        following_list = self.following[followerId]
        if followeeId in following_list:
            following_list.remove(followeeId)
        
