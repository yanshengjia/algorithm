"""
Given a text file file.txt, print just the 10th line of the file.

Example:

Assume that file.txt has the following content:

Line 1
Line 2
Line 3
Line 4
Line 5
Line 6
Line 7
Line 8
Line 9
Line 10
Your script should output the tenth line, which is:
Line 10

Follow up:
1. If the file contains less than 10 lines, what should you output?
2. There's at least three different solutions. Try to explore all possibilities.


Solution:
1. head/tail
2. sed
3. awk
"""

# Simply using the combination of the head and tail commands is probably the easiest approach. Below is an example using head and tail to read the 10th line of file.txt:
# This solution can not solve the situation which file has less than 10 lines.
cat file.txt | head -10 | tail -1


# There are a couple of nice ways to do this with sed. 
# The first is with the p (print) command, and the other is with the d (delete) command.
# The n option with the print command is used to only print lines explicitly indicated by the command.
# For example, sed will output the 10th line of file.txt with each of the commands below:

#print/p command
cat file.txt | sed -n '10p'  # > 73%
 
#delete/d command
cat file.txt | sed '10!d'  # > 73%


# awk has a built in variable NR that keeps track of file/stream row numbers.
# awk syntax and idioms can be hard to read, so below are three different ways to print line 10 of file.txt file using awk.
cat file.txt | awk 'NR==10'     # > 73%
cat file.txt | awk 'NR==10{print}'  # > 100%
cat file.txt | awk '{if(NR==10) print}'  # >73%