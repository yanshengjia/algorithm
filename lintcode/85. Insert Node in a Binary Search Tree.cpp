// Author: Shengjia Yan
// Date: 2017年7月29日
// Email: sjyan@seu.edu.cn
// Time Complexity: O(n) n为二叉查找树的节点个数
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
     * @param root: The root of the binary search tree.
     * @param node: insert this node into the binary search tree
     * @return: The root of the new binary search tree.
     */
    TreeNode* insertNode(TreeNode* root, TreeNode* node) {
        // write your code here
        if (root == NULL)   root = node;
        else if (root->val < node->val)  root->right = insertNode(root->right, node);
        else if (root->val > node->val)  root->left = insertNode(root->left, node);
        return root;
    }
};