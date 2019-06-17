// Author: Shengjia Yan
// Date: 2017年7月22日
// Email: sjyan@seu.edu.cn
// Time Complexity: O(n) n为链表长度
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
     * @return: head node
     */
    ListNode *deleteDuplicates(ListNode *head) {
        // write your code here
        if (head == NULL || head->next == NULL) return head;
        
        ListNode *h = head, *p = h->next, *q = p->next;
        
        while (1) {
            if (h->val == p->val) {
                h->next = q;
            } else {
                h = h->next;
            }
            p = p->next;
            if (p == NULL) return head;
            q = q->next;
        }
    }
};


class Solution {
public:
    /**
     * @param head: head is the head of the linked list
     * @return: head of linked list
     */
    ListNode * deleteDuplicates(ListNode * head) {
        // write your code here
        ListNode *cur = head;
        
        while (cur && cur->next) {
            if (cur->val == cur->next->val) {
                cur->next = cur->next->next;
            }
            else {
                cur = cur->next;
            }
        }
        
        return head;
    }
};