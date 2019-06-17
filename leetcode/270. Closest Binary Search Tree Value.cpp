// Author: Shengjia Yan
// Date: 2018-05-21 Monday
// Email: i@yanshengjia.com
// Time Complexity: O(n/2)
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
    int closestValue(TreeNode* root, double target) {
        int res = root->val;
        while (root) {
            if (abs(res - target) >= abs(root->val - target)) {
                res = root->val;
            }
            root = root->val < target ? root->right : root->left;
        }
        return res;
    }
};