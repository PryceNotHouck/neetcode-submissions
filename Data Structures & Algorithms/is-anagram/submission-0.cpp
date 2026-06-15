#include <vector>
class Solution {
public:
    bool isAnagram(string s, string t) {
        vector<char> si(s.begin(), s.end());
        vector<char> ti(t.begin(), t.end());

        std::sort(si.begin(), si.end());
        std::sort(ti.begin(), ti.end());

        if (si == ti) {
            return true;
        }
        return false;
    }
};
