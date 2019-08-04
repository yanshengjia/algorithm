// Author: Shengjia Yan
// Date: 2017年7月1日
// Email: sjyan@seu.edu.cn
// Time Complexity: O(logn)
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
     * @param root: a TreeNode, the root of the binary tree
     * @return: nothing
     */
    TreeNode *temp;
    void invertBinaryTree(TreeNode *root) {
        // write your code here
        if (root != NULL) {
            temp = root->left;
            root->left = root->right;
            root->right = temp;
            invertBinaryTree(root->left);
            invertBinaryTree(root->right);
        }
    }
};