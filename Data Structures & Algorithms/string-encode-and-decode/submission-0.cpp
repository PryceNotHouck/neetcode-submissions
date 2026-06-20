class Solution {
public:

    string encode(vector<string>& strs) {
        string result = "";
        for(auto& it : strs) {
            result.append(it);
            result.append(".");
        }

        return result;
    }

    vector<string> decode(string s) {
        vector<string> result;
        string temp;
        for(auto& it : s) {
            if(it == '.') {
                result.push_back(temp);
                temp = "";
            } else {
                temp.push_back(it);
            }
        }

        return result;
    }
};
