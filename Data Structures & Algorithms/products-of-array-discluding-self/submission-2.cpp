// Follow Up
#include <algorithm>
#include <numeric>

class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> results;
        for(int i = 0; i < nums.size(); i++) {
            vector<int> temp = nums;
            temp.erase(temp.begin() + i);
            results.push_back(std::accumulate(temp.begin(), temp.end(), 1, multiplies<void>{}));
        }
        return results;
    }
};
