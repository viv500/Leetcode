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

        for aid, account in enumerate(accounts):
            name, *emails = account

            for email in emails:
                if email in email_to_id:
                    union(aid, email_to_id[email])
                
                email_to_id[email] = aid

        print(email_to_id)
        print(parent)

        account_emails = defaultdict(list)

        for index, p in enumerate(parent):
            name, *emails = accounts[index]
            account_emails[(find(index), name)].extend(emails)
        print(account_emails)

        result = []

        for aid, name in account_emails:
            emails = account_emails[(aid, name)]
            result.append(list(set([name] + sorted(emails))))

        return result



