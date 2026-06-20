#include <map>
using namespace std;

class Solution {
public:
    static bool compare(pair<int, int>& a, pair<int, int>& b) {
        return a.second > b.second;
    }

    vector<int> topKFrequent(vector<int>& nums, int k) {
        map<int, int> counts;
        for (int i = 0; i < nums.size(); i++) {
            counts[nums[i]] += 1;
        }

        vector<pair<int, int>> deMap;
        for (auto& it : counts) {
            deMap.push_back(it);
        }
        sort(deMap.begin(), deMap.end(), compare);

        vector<int> result;
        for (int i = 0; i < k; i++) {
            cout << deMap[i].first << " " << deMap[i].second << "\n";
            result.push_back(deMap[i].first);
        }
        return result;
    }
};
