// Author: Shengjia Yan
// Date: 2017年8月6日
// Email: sjyan@seu.edu.cn
// Time Complexity: O(n)  n是数组长度
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
public:
    /**
     * @param A: A sorted (increasing order) array
     * @return: A tree node
     */
    TreeNode *sortedArrayToBST(vector<int> &A) {
        // write your code here
        TreeNode *root = NULL;
        
        if (A.empty())
            return NULL;
        
        int size = A.size();
        int low = 0, high = size - 1;
        
        root = createTree(A, low, high);
        
        return root;
    }
    
    TreeNode *createTree(vector<int> &A, int low, int high) {
        TreeNode *root;
        
        if (low > high)
            return NULL;
        
        int mid = (low + high) / 2;
        root = new TreeNode(A[mid]);
        root->left = createTree(A, low, mid - 1);
        root->right = createTree(A, mid + 1, high);
        
        return root;
    }
};