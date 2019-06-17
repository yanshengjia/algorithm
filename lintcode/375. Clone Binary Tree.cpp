// Author: Shengjia Yan
// Date: 2017年7月21日
// Email: sjyan@seu.edu.cn
// Time Complexity: O(n)
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
     * @param root: The root of binary tree
     * @return root of new tree
     */
    TreeNode* cloneTree(TreeNode *root) {
        // Write your code here
        if (root != NULL) {
            TreeNode *newroot = new TreeNode(root->val);
            
            if (root->left != NULL)
                newroot->left = cloneTree(root->left);
            if (root->right != NULL)
                newroot->right = cloneTree(root->right);
            
            return newroot;
        }
        return NULL;
    }
};