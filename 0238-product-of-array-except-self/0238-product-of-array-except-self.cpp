#include <vector>

class Solution {
public:
    std::vector<int> productExceptSelf(std::vector<int>& nums) {
        int length = nums.size();
        std::vector<int> result(length, 1);

        // Calculate product of all elements to the left of each element
        int left_product = 1;
        for (int i = 0; i < length; ++i) {
            result[i] *= left_product;
            left_product *= nums[i];
        }

        // Calculate product of all elements to the right of each element
        int right_product = 1;
        for (int i = length - 1; i >= 0; --i) {
            result[i] *= right_product;
            right_product *= nums[i];
        }

        return result;
    }
};
