// Author: Shengjia Yan
// Date: 2017年7月7日
// Email: sjyan@seu.edu.cn
// Time Complexity: O(m+n)
// Space Complexity: O(max(m, n))


/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    /**
     * @param l1: the first list
     * @param l2: the second list
     * @return: the sum list of l1 and l2 
     */
    ListNode *addLists(ListNode *l1, ListNode *l2) {
        // write your code here
        ListNode *result = NULL, *iter = NULL, *i = l1, *j = l2;
        int val1 = 0, val2 = 0, carry = 0, sum = 0;
        
        if (i == NULL && j == NULL) {
            return NULL;
        }
        else if (i == NULL) {
            return j;
        }
        else if (j == NULL) {
            return i;
        }
        else {
            while (i != NULL && j != NULL) {
                val1 = i->val;
                val2 = j->val;
                sum = (val1 + val2 + carry) % 10;
                carry = (val1 + val2 + carry) / 10;
                ListNode *node = new ListNode(sum);
                
                if (result == NULL) {
                    result = node;
                }
                
                if (iter != NULL) {
                    iter->next = node;
                }
                
                iter = node;
                i = i->next;
                j = j->next;
            }
            
            while (i != NULL) {
                sum = (i->val + carry) % 10;
                carry = (i->val + carry) / 10;
                ListNode *node = new ListNode(sum);
                
                iter->next = node;
                
                iter = node;
                i = i->next;
            }
            
            while (j != NULL) {
                sum = (j->val + carry) % 10;
                carry = (j->val + carry) / 10;
                ListNode *node = new ListNode(sum);
                
                iter->next = node;
                
                iter = node;
                j = j->next;
            }
            
            if (carry) {
                ListNode *node = new ListNode(carry);
                iter->next = node;
            }
            
            return result;
        }
    }
};