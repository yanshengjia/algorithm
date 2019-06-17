// Author: Shengjia Yan
// Date: 2018-05-30 Wednesday
// Email: i@yanshengjia.com


/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

// recursive method
// Time Complexity: O(n)
// Space Complexity: O(1)
class Solution {
public:
    bool isSymmetric(TreeNode* root) {
        if (!root)  return true;
        return helper(root->left, root->right);
    }
    
    bool helper(TreeNode *root1, TreeNode *root2) {
        if (!root1 && !root2)   return true;
        else if (!root1 || !root2)   return false;
        else {
            if (root1->val != root2->val)   return false;
            return helper(root1->left, root2->right) && helper(root1->right, root2->left);
        }
    }
};


// iterative method
class Solution {
public:
    bool isSymmetric(TreeNode* root) {
        if (!root) return true;
        queue<TreeNode*> q1, q2;
        q1.push(root->left);
        q2.push(root->right);
        
        while (!q1.empty() && !q2.empty()) {
            TreeNode *node1 = q1.front();
            TreeNode *node2 = q2.front();
            q1.pop();
            q2.pop();
            if((node1 && !node2) || (!node1 && node2)) return false;
            if (node1) {
                if (node1->val != node2->val) return false;
                q1.push(node1->left);
                q1.push(node1->right);
                q2.push(node2->right);
                q2.push(node2->left);
            }
        }
        return true;
    }
};