#include <map>

class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        map<int, bool> seen;
        for (int i = 0; i < nums.size(); i++) {
            if (seen[nums[i]] == true) {
                return true;
            } else {
                seen[nums[i]] = true;
            }
        }
        return false;
    }
};