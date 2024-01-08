/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public int rangeSumBST(TreeNode root, int low, int high) {
        int sum = 0;
        
        if(root == null){
            return 0;
        }
        else if(root.val < low){ // low 보다 낮으니까 오른쪽으로
            return rangeSumBST(root.right, low, high);
        }
        else if(root.val > high){ // high 보다 높으니까 왼쪽으로
            return rangeSumBST(root.left, low, high);
        }
        // low, high 사이에 있는 값은 더한다.
        return root.val + rangeSumBST(root.right, low, high) + rangeSumBST(root.left, low, high);
        
    }
}