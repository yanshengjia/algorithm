"""
Given a text file file.txt that contains list of phone numbers (one per line), write a one liner bash script to print all valid phone numbers.

You may assume that a valid phone number must appear in one of the following two formats: (xxx) xxx-xxxx or xxx-xxx-xxxx. (x means a digit)

You may also assume each line in the text file must not contain leading or trailing white spaces.

Example:

Assume that file.txt has the following content:

987-123-4567
123 456 7890
(123) 456-7890
Your script should output the following valid phone numbers:

987-123-4567
(123) 456-7890


Solution:
1. grep
2. sed
3. awk
https://www.cnblogs.com/grandyang/p/5389375.html
"""

# Using grep:
grep -P '^(\d{3}-|\(\d{3}\) )\d{3}-\d{4}$' file.txt

# Using sed:
sed -n -r '/^([0-9]{3}-|\([0-9]{3}\) )[0-9]{3}-[0-9]{4}$/p' file.txt

# Using awk:
"""
这道题是难点是如何写匹配的正则表达式。那么首先来看‘/.../'表示中间的是要匹配的正则表达式，然后脱字符^匹配一行的开头，美元符$在正则表达式中匹配行尾，然后再看中间的部分，[0-9]{3}表示匹配三个数字，圆括号括起一组正则表达式. 它和"|"操作符或在用expr进行子字符串提取(substring extraction)一起使用很有用。那么([0-9]{3}-|[0−9]3 )就可以理解了，它匹配了xxx-和(xxx) 这两种形式的字符串，然后后面的就好理解了，匹配xxx-xxxx这样的字符串.
"""
awk '/^ ([0-9]{3}- | \([0-9]{3}\)) [0-9]{3}-[0-9]{4} $/' file.txt