// Author: Shengjia Yan
// Date: 2017年7月20日
// Email: sjyan@seu.edu.cn
// Time Complexity: O(1)
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
     * @param node: a node in the list should be deleted
     * @return: nothing
     */
    void deleteNode(ListNode *node) {
        // write your code here
        ListNode *p = node->next, *q = p->next;
        node->val = p->val;
        
        if (q == NULL) {
            node->next = NULL;
        } else {
          node->next = q;  
        }
    }
};