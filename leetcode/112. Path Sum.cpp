// Author: Shengjia Yan
// Date: 2018-05-25 Friday
// Email: i@yanshengjia.com
// Time Complexity: O(n)
// Space Complexity: O(1)

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    bool hasPathSum(TreeNode* root, int sum) {
        if (!root)  return false;
        int top = root->val;
        if (!root->left && !root->right && top == sum) return true;
        
        bool left = hasPathSum(root->left, sum-top);
        bool right = hasPathSum(root->right, sum-top);
        
        if (left || right)  return true;
        else return false;
    }
};