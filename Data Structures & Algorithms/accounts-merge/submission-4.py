from collections import defaultdict
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parent = list(range(len(accounts)))
        email_to_id = {}
        name_id_to_emails = defaultdict(set)

        def find(a):
            while a != parent[a]:
                parent[a] = parent[parent[a]]
                a = parent[a]

            return a

        def union(a, b):
            parent[find(a)] = find(b)

        for i, a in enumerate(accounts):
            name, *emails = a

            for email in emails:
                if email in email_to_id:
                    union(i, email_to_id[email])
                else:
                    email_to_id[email] = i

        for i,p in enumerate(parent):
            name = accounts[i][0]
            emails = accounts[i][1:]
            component = find(i)
            for e in emails:
                name_id_to_emails[(name, component)].add(e)


        return [[a[0]] + sorted(name_id_to_emails[a]) for a in name_id_to_emails]



