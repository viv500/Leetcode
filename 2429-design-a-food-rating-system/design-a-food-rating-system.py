from collections import defaultdict
import heapq
class FoodRatings:

    def __init__(self, foods: list[str], cuisines: list[str], ratings: list[int]):
        self.cuisine_foods = {}
        self.food_ratings = {}
        self.food_to_cuisine = {}

        for food, cuisine, rating in zip(foods, cuisines, ratings):
            self.food_ratings[food] = rating
            if cuisine not in self.cuisine_foods:
                self.cuisine_foods[cuisine] = []
            heapq.heappush(self.cuisine_foods[cuisine], (-rating, food))

            self.food_to_cuisine[food] = cuisine


    def changeRating(self, food: str, newRating: int) -> None:
        self.food_ratings[food] = newRating
        heapq.heappush(self.cuisine_foods[self.food_to_cuisine[food]], (-newRating, food))
        
    def highestRated(self, cuisine: str) -> str:
        heap = self.cuisine_foods[cuisine]

        while heap and -heap[0][0] != self.food_ratings[heap[0][1]]:
            heapq.heappop(heap)

        return heap[0][1]
        


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)