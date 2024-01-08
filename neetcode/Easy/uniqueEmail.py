class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        s = set()
        for email in emails:
            emailSplit = email.split('@')
            emailSplit[0] = emailSplit[0].replace('.', '')
            if emailSplit[0].find('+') > 0:
                index = emailSplit[0].find('+')
                emailSplit[0] = emailSplit[0][:index]
            
            s.add(emailSplit[0] + "@" + emailSplit[1])
        return len(s)
