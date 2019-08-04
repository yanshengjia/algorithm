// Author: Shengjia Yan
// Date: 2017年7月1日
// Email: sjyan@seu.edu.cn
// Time Complexity: O(m+n)
// Space Complexity: O(m+n)


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
class Recursion {
public:
    /**
     * @param ListNode l1 is the head of the linked list
     * @param ListNode l2 is the head of the linked list
     * @return: ListNode head of linked list
     */
    ListNode *mergeTwoLists(ListNode *l1, ListNode *l2) {
        // write your code here
        if (!l1)
            return l2;
        else if (!l2)
            return l1;
        
        ListNode *result = NULL;
        
        if (l1->val < l2->val) {
            result = l1;
            result->next = mergeTwoLists(l1->next, l2);
        }
        else {
            result = l2;
            result->next = mergeTwoLists(l1, l2->next);
        }
        
        return result;
    }
};

class NonRecursion {
public:
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        ListNode *guard = new ListNode(0);
        ListNode *current = guard;

        while (l1 != NULL && l2 != NULL) {
            if (l1->val < l2->val) {
                current->next = l1;
                l1 = l1->next;
            } else {
                current->next = l2;
                l2 = l2->next;
            }
            current = current->next;
        }

        if (l1 != NULL) {
            current->next = l1;
        } else {
            current->next = l2;
        }
        
        return guard->next;
    }
};