class Solution:
    def bestTeamScore(self, scores: list[int], ages: list[int]) -> int:
        player_info = list(zip(ages, scores))
        player_info.sort()
        print(player_info)

        dp = [s for _, s in player_info]

        for i in range(len(scores)):
            for j in range(i):
                a = player_info[j][1]
                b = player_info[i][1]
                if a <= b:
                    dp[i] = max(dp[i], dp[j] + b)

        return max(dp)