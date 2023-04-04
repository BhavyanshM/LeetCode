#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int i = 0;
        int j = nums.size() - 1;

        unordered_map<int, int> map;
        unordered_map<int, int> repeat_map;

        for (int m = 0; m<nums.size(); m++)
        {
            if(!map.count(nums[m]))
            {
                map[nums[m]] = m;
            }
            else
            {
                repeat_map[nums[m]] = m;
            }
        }

        std::sort(nums.begin(), nums.end());

        vector<int> indices;

        for (int k = 0; k<nums.size(); k++)
        {
            if (nums[i] + nums[j] < target)
            {
                i++;
            }
            else if (nums[i] + nums[j] > target)
            {
                j--;
            }
            else 
            {
                indices.push_back(map[nums[i]]);

                if (nums[i] != nums[j])
                {
                    indices.push_back(map[nums[j]]);
                }
                else
                {
                    indices.push_back(repeat_map[nums[j]]);
                }

                break;
            }

            if (i == j)
            {
                break;
            }
        }

        return indices;
    }
};

int main()
{
    using namespace std; 

    vector<int> nums = { 2, 3, 3, 7, 11, 15 };
    int target = 10;

    Solution solution;
    vector<int> indices = solution.twoSum(nums, target);

    for (int i = 0; i<indices.size(); i++)
    {
        cout << indices[i] << endl;
    }

    return 0;
}