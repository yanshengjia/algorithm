// Author: Shengjia Yan
// Date: 2017年7月1日
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
     * @param root: The root of binary tree.
     * @return: An integer
     */
    int minDepth(TreeNode *root) {
        // write your code here
        if (!root)  return 0;
        int left_depth = minDepth(root->left);
        int right_depth = minDepth(root->right);
        if (!left_depth)    return right_depth + 1;
        if (!right_depth)   return left_depth + 1;
        return left_depth > right_depth ? right_depth + 1 : left_depth + 1;
    }
};