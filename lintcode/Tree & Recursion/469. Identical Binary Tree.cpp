// Author: Shengjia Yan
// Date: 2017年7月21日
// Email: sjyan@seu.edu.cn
// Time Complexity: O(n) n为二叉树节点个数
// Space Complexity: O(1)


/**
 * Definition of TreeNode:
 * class TreeNode {
 * public:
 *     int val;
 *     TreeNode *left, *right;
 *     TreeNode(int val) {
 *         this->val = val;
 *         this->left = this->right = NULL;
 *     }
 * }
 */
class Solution {
public:
    /**
     * @aaram a, b, the root of binary trees.
     * @return true if they are identical, or false.
     */
    bool isIdentical(TreeNode* a, TreeNode* b) {
        // Write your code here
        if (a == NULL && b == NULL) return true;
        
        if (a != NULL && b != NULL && a->val == b->val) {
            return isIdentical(a->left, b->left) && isIdentical(a->right, b->right);
        } else {
            return false;
        }
    }
};