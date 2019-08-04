// Author: Shengjia Yan
// Date: 2017年8月13日
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
     * @return: The head of linked list.
     */
    ListNode *removeNthFromEnd(ListNode *head, int n) {
        // write your code here
        if (head == NULL)
            return head;
        
        int length = 0, count = 0;
        ListNode *iter = head;
        
        while (iter != NULL) {
            length++;
            iter = iter->next;
        }
        
        int target = length - n;
        
        if (target == 0) {
            head = head->next;
            return head;
        }
        else {
            iter = head;
            
            while (iter != NULL) {
                if (count == target - 1) {
                    iter->next = iter->next->next;
                    return head;
                }
                
                count++;
                iter = iter->next;
            }
        }
    }
};


