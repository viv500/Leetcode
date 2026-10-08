from collections import defaultdict
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        def union(a, b):
            parent[find(a)] = find(b)

        def find(a):
            while a != parent[a]:
                parent[a] = parent[parent[a]]
                a = parent[a]

            return a

        parent = list(range(len(accounts)))
        email_to_id = {}

        for aid, (_, *emails) in enumerate(accounts):
            for email in emails:
                if email in email_to_id:
                    union(aid, email_to_id[email])
                else:     
                    email_to_id[email] = aid

        groups = defaultdict(set)

        for email in email_to_id:
            index = find(email_to_id[email])
            groups[index].add(email)

        return [[accounts[e][0]] + sorted(groups[e]) for e in groups]