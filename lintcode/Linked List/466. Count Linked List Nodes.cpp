// Author: Shengjia Yan
// Date: 2018-04-08 Sunday
// Email: i@yanshengjia.com
// Time Complexity: O(n)
// Space Complexity: O(1)


// Definition of ListNode
class ListNode {
public:
    int val;
    ListNode *next;
    ListNode(int val) {
        this->val = val;
        this->next = NULL;
    }
};


class Solution {
public:
    /*
     * @param head: the first node of linked list.
     * @return: An integer
     */
    int countNodes(ListNode * head) {
        // write your code here
        int count = 0;
        while (head != NULL) {
            head = head -> next;
            count++;
        }
        return count;
    }
};