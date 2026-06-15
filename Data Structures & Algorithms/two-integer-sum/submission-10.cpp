#include <map>
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        map<int, int> sums;
        for (int i = 0; i < nums.size(); i++) {
            sums[target - nums[i]] = i;
        }
        for (int j = 0; j < nums.size(); j++) {
            if (sums.find(nums[j]) != sums.end() && sums[nums[j]] != j) {
                return {j, sums[nums[j]]};
            }
        }
    }
};
