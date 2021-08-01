"""
Given a text file file.txt, transpose its content.

You may assume that each row has the same number of columns, and each field is separated by the ' ' character.

Example:

If file.txt has the following content:

name age
alice 21
ryan 30
Output the following:

name alice ryan
age 21 30


Solution:
awk
1. The code block with an `END` prefix is only executed after the last line is read; similarly, a code block with a `BEGIN` prefix will be executed before any line reads.

2. AWK is line-based: the main code block (the code block without prefix, the for loop) processes one line of input at a time.

3. NR: number of records (i.e. current line number) that's accumulated across multiple files read.

4. NF: number of fields (i.e. number of `columns`) on an input line.

5. $i: the i-th field of the input line.

6. s[]: an array for saving the transposed table.
"""


# Read from the file file.txt and print its transposed content to stdout.
awk '
{
    for (i = 1; i <= NF; i++) {
        if (NR == 1) {
            s[i] = $i;
        } else {
            s[i] = s[i] " " $i;
        }
    }
}
END {
    for (i = 1; s[i] != ""; i++) {
        print s[i];
    }
}' file.txt
