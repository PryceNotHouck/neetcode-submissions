class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        if(!nums.size()) {
            return 0;
        }

        sort(nums.begin(), nums.end());
        auto dupes = unique(nums.begin(), nums.end());
        nums.erase(dupes, nums.end());

        int result = 1;
        int temp = 1;
        for(int i = 1; i < nums.size(); i++) {
            if(nums[i] == nums[i - 1] + 1) {
                temp++;
            } else {
                temp = 1;
            }
            if(temp > result) {
                    result = temp;
                }
        }
        return result;
    }
};
