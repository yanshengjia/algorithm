"""
Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.

Example 1:

Input: a = 1, b = 2
Output: 3
Example 2:

Input: a = -2, b = 3
Output: 1


Solution:
Bit Manipulation

不能用加号或者其他什么数学运算符号，那么我们只能回归计算机运算的本质，位操作 Bit Manipulation，我们在做加法运算的时候，每位相加之后可能会有进位 Carry 产生，然后在下一位计算时需要加上进位一起运算，那么我们能不能将两部分拆开呢，我们来看一个例子 759+674

1. 如果我们不考虑进位，可以得到 323
2. 如果我们只考虑进位，可以得到 1110
3. 我们把上面两个数字假期 323+1110=1433 就是最终结果了

然后我们进一步分析，如果得到上面的第一第二种情况，我们在二进制下来看，不考虑进位的加，0+0=0，0+1=1, 1+0=1，1+1=0，这就是异或(XOR)的运算规则，如果只考虑进位的加 0+0=0, 0+1=0, 1+0=0, 1+1=1，而这其实这就是'与'(AND)的运算，而第三步在将两者相加时，我们再递归调用这个算法，终止条件是当进位为0时，直接返回第一步的结果。

Error:
Line 5: Char 33: runtime error: left shift of negative value -2147483648 (solution.cpp)
LeetCode 自己的编译器比较 strict，不能对负数进行左移，就是说最高位符号位必须要为0，才能左移。那么我们在a和b相'与'之后，再'与'上一个最高位为0，其余位都为1的数 0x7fffffff，这样可以强制将最高位清零，然后再进行左移.

Basically here is the intuitive explanation:

1. a ^ b we know gives us sum value WITH ALL DIGITS ADDED without carry: 0 ^ 0 = 0 , 1 ^ 0 = 1, 0 ^ 1 = 1, 1 ^ 1 = 0, this is what the sum of each digit should be without thinking of the carry.
2. How to get carry of each digit position? we do & of course. 1 + 1 is the only combination that gives a carry: so we use 1&1 because only with & operator you get 1 when 1&1 and you get 0 for all other combinations. This stuff is obvious.
3. Why left shift? because each carry digit has to be added to the sum of the immediate left digits.
4. Why b == 0 at some point? Because you could have the carry being added to a sum and still generate a carry. Think of this situation 1+0+1 or 0+1+1 or 1+1+1 or 1+1+0. In these cases you will have another carry that has to be further added.
5. At some point when all carries from subsequent additions will be done being properly added within the final result, there will be no more carries in the addition. At this point your sum becomes the final answer and the number which is supposed to be the carry becomes 0. At this point b ==0.
"""


class Solution {
public:
    int getSum(int a, int b) {
        while (b != 0) {
            int carry = (a & b & 0x7fffffff) << 1;  // calculate the carry, limited to 32 bits
            a = a ^ b;  // calculate sum and b(carry)
            b = carry;
        }
        return a;
    }
};