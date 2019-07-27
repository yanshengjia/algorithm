"""
Every email consists of a local name and a domain name, separated by the @ sign.

For example, in alice@leetcode.com, alice is the local name, and leetcode.com is the domain name.

Besides lowercase letters, these emails may contain '.'s or '+'s.

If you add periods ('.') between some characters in the local name part of an email address, mail sent there will be forwarded to the same address without dots in the local name.  For example, "alice.z@leetcode.com" and "alicez@leetcode.com" forward to the same email address.  (Note that this rule does not apply for domain names.)

If you add a plus ('+') in the local name, everything after the first plus sign will be ignored. This allows certain emails to be filtered, for example m.y+name@email.com will be forwarded to my@email.com.  (Again, this rule does not apply for domain names.)

It is possible to use both of these rules at the same time.

Given a list of emails, we send one email to each address in the list.  How many different addresses actually receive mails? 

 

Example 1:

Input: ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
Output: 2
Explanation: "testemail@leetcode.com" and "testemail@lee.tcode.com" actually receive mails


Solution:
simulation problem
"""


# time-O(n), where n is the length of list emails
# space-O(m), where m is the number of unique emails
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        d = dict()
        res = 0
        for i in range(len(emails)):
            s = emails[i].split('@')
            local, domain = s[0], s[1]
            local = local.replace('.', '')
            local = local.split('+')[0]
            emails[i] = '{}@{}'.format(local, domain)
            if emails[i] not in d:
                d[emails[i]] = 1
                res += 1
            else:
                d[emails[i]] += 1
        return res
            

# time-O(n), where n is the length of list emails
# space-O(m), where m is the number of unique emails
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        d = set()
        res = 0
        for i in range(len(emails)):
            local, domain = emails[i].split('@')
            local = local.replace('.', '')
            local = local.split('+')[0]
            emails[i] = '{}@{}'.format(local, domain)
            d.add(emails[i])
        return len(d)