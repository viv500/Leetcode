class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        def compressed(email: str) -> str:

            domain = email.split("@")[1]
            local = email.split("@")[0]

            for i in range(len(local)):
                if local[i] == '+':
                    local = local[0: i]
                    break

            no_periods = ''.join(local.split("."))

            return no_periods + "@" + domain
        
        unique = set()
        vals = 0

        for email in emails:
            if compressed(email) not in unique:
                vals += 1
                unique.add(compressed(email))

        return vals





        




        