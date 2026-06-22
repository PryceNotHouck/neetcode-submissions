class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> result;
        int product;
        for(int i = 0; i < nums.size(); i++) {
            product = nums[0];
            for(int j = 1; j < nums.size(); j++) {
                if(nums[i] == 0 && i == j) {
                    product = product;
                } else {
                    product *= nums[j];
                }
            }

            if(nums[i] == 0) {
                result.push_back(product);
            } else {
                product /= nums[i];
                result.push_back(product);
            }
        }
        return result;
    }
};
