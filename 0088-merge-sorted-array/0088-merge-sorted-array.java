import java.util.Arrays;

class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int length = m + n;
        int[] resultArray = new int[length];
        
        System.arraycopy(nums2, 0, nums1, m, n);
        
        Arrays.sort(nums1);

    }
}