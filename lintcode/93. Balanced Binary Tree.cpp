// Author: Shengjia Yan
// Date: 2017年8月1日
// Email: sjyan@seu.edu.cn
// Time Complexity: O(2n) n为二叉树中节点个数
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
     * @param root: The root of binary tree.
     * @return: True if this Binary tree is Balanced, or false.
     */
    int depth(TreeNode *root) {
        if (root == NULL) {
            return 0;
        }
        return max(depth(root->left), depth(root->right)) + 1;
    }
    
    bool isBalanced(TreeNode *root) {
        // write your code here
        if (root == NULL)    return true;
        
        if (!isBalanced(root->left))    return false;
        if (!isBalanced(root->right))   return false;
        
        int left_depth = depth(root->left);
        int right_depth = depth(root->right);
        
        if (abs(left_depth - right_depth) > 1) return false;
        
        return true;
    }
};
