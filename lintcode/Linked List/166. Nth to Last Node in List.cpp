// Author: Shengjia Yan
// Date: 2017年7月1日
// Email: sjyan@seu.edu.cn
// Time Complexity: O(n)
// Space Complexity: O(1)


/**
 * Definition of ListNode
 * class ListNode {
 * public:
 *     int val;
 *     ListNode *next;
 *     ListNode(int val) {
 *         this->val = val;
 *         this->next = NULL;
 *     }
 * }
 */
class Solution {
public:
    /**
     * @param head: The first node of linked list.
     * @param n: An integer.
     * @return: Nth to last node of a singly linked list. 
     */
    ListNode *nthToLast(ListNode *head, int n) {
        // write your code here
        int size = 0;
        int i = 0;
        ListNode *p = head;
        
        while(p != NULL) {
            p = p->next;
            size++;
        }
        
        int pos = size - n;
        
        while(head != NULL) {
            if (i == pos)   return head;
            head = head->next;
            i++;
        }
    }
};


