#include <map>
#include <algorithm>

class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> results;
        map<int, vector<pair<int, int>>> twoSum;

        for(int i = 0; i < nums.size(); i++) {
            int fixed = nums[i];
            for(int j = i + 1; j < nums.size(); j++) {
                twoSum[0 - (nums[i] + nums[j])].push_back({i, j});
            }
        }

        for(int i = 0; i < nums.size(); i++) {
            if(twoSum.contains(nums[i])) {
                for(auto& p : twoSum[nums[i]]) {
                    if(i != p.first && i != p.second) {
                        vector<int> temp = {nums[i], nums[p.first], nums[p.second]};
                        sort(temp.begin(), temp.end());
                        
                        if(find(results.begin(), results.end(), temp) == results.end()) {
                            results.push_back(temp);
                        }
                    }
                }
            }
        }

        return results;
    }
};
