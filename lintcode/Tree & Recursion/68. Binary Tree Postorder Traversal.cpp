// Author: Shengjia Yan
// Date: 2017年7月1日
// Email: sjyan@seu.edu.cn
// Time Complexity: O(n)
// Space Complexity: O(n)


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
    /**
     * @param root: The root of binary tree.
     * @return: Postorder in vector which contains node values.
     */
public:
    vector<int> result;
    vector<int> postorderTraversal(TreeNode *root) {
        // write your code here
        if (root == NULL) {
            return result;
        }
        else {
            postorderTraversal(root->left);
            postorderTraversal(root->right);
            result.push_back(root->val);
        }
        return result;
    }
};