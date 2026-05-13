from collections import defaultdict
import heapq
class Twitter:

    # similar to merge k sorted lists

    def __init__(self):
        self.following = defaultdict(set) # user id -> set of followeeIds
        self.user_posts = defaultdict(list) # user id -> list of (tweet_count, tweet_id)
        self.tweet_count = 0 

    def postTweet(self, userId: int, tweetId: int) -> None:
        user_posts = self.user_posts[userId]

        self.tweet_count += 1
        user_posts.append((self.tweet_count, tweetId))


        print(user_posts)
    

    def getNewsFeed(self, userId: int) -> List[int]:
        following = self.following[userId]
        maxHeap = []
        output = []

        # init with the most recent post from each follower
        # needed to grab users own recent posts too !
        self.following[userId].add(userId)

        for followee in following:
            # does the user have at least 1 post?
            if followee in self.user_posts:
                tweet_count, tweet_id = self.user_posts[followee][-1]
                index = len(self.user_posts[followee]) - 1 # to grab the final index
                heapq.heappush_max(maxHeap, (tweet_count, tweet_id, followee, index)) # need to push followee id and index so we know which entry to access

        while maxHeap and len(output) < 10:
            _, tweet_id, followee, index = heapq.heappop_max(maxHeap)
            output.append(tweet_id)
            if index > 0:
                index -= 1
                tweet_count, tweet_id = self.user_posts[followee][index]
                heapq.heappush_max(maxHeap, (tweet_count, tweet_id, followee, index))

        
        return output
        

        

    def follow(self, followerId: int, followeeId: int) -> None:
        following = self.following[followerId]
        following.add(followeeId)
        
    def unfollow(self, followerId: int, followeeId: int) -> None:
        following = self.following[followerId]
        if followeeId in following:
            following.remove(followeeId)
        
