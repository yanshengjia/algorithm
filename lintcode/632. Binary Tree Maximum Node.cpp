// Author: Shengjia Yan
// Date: 2017年7月1日
// Email: sjyan@seu.edu.cn
// Time Complexity: O(n)
// Space Complexity: O(1)


class Solution {
public:
    /**
     * @param root the root of binary tree
     * @return the max node
     */
    TreeNode* max = new TreeNode(-99999);
    TreeNode* maxNode(TreeNode* root) {
        // Write your code here
        if (root == NULL) {
            return NULL;
        }
        else {
            if (root->val > max->val) {
                max = root;
            }
            maxNode(root->left);
            maxNode(root->right);
        }
        return max;
    }
};