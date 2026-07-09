class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& nums) {
        int maxConsecutive = 0;
        int currentCount = 0;
        for (int num : nums){
            if (num == 1){
                currentCount++;
                maxConsecutive = max(maxConsecutive, currentCount);
            }
            else{
                currentCount = 0;
            }
        }
        return maxConsecutive;
    }
};