// Author: Shengjia Yan
// Date: 2017年8月8日
// Email: sjyan@seu.edu.cn
// Time Complexity: O(n)  n是树的节点个数
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
     * @param root the root of binary tree
     * @return the new root
     */
    void traversal(TreeNode *root, int &sum) {
        if (root == NULL)  return;
        traversal(root->right, sum);
        root->val += sum;
        sum = root->val;
        traversal(root->left, sum);
    }
    
    TreeNode* convertBST(TreeNode* root) {
        // Write your code here
        int sum = 0;
        traversal(root, sum);
        return root;
    }
};