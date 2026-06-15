#include <set>

class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        set<int> seen(nums.begin(), nums.end());
        if (seen.size() == nums.size()) {
            return false;
        }
        return true;
    }
};