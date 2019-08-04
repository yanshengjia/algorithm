// Author: Shengjia Yan
// Date: 2018-05-27 Sunday
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
    TreeNode* deleteNode(TreeNode* root, int key) {
        if (!root)  return NULL;
        
        if (root->val < key) {
            root->right = deleteNode(root->right, key);
        }
        else if (root->val > key) {
            root->left = deleteNode(root->left, key);
        }
        else {
            if (!root->left || !root->right) {
                root = (root->left) ? (root->left) : (root->right);
            }
            else {
                TreeNode *cur = root->right;
                while (cur->left)   cur = cur->left;
                root->val = cur->val;
                root->right = deleteNode(root->right, cur->val);
            }  
        }
        
        return root;
    }
};