class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        for(int i = 0; i < numbers.size(); i++) {
            int temp = target - numbers[i];
            int left = i + 1;
            int right = numbers.size() - 1;
            while(left <= right) {
                int mid = left + (right - left) / 2;
                if(temp == numbers[mid]) {
                    return {i + 1, mid + 1};
                } else if(temp > numbers[mid]) {
                    left = mid + 1;
                } else {
                    right = mid - 1;
                }
            }
        }
        return {};
    }
};
