#include <iostream>
#include <vector>
using namespace std;

class Solution
{
public:
    double findMedianSortedArrays(vector<int> &nums1, vector<int> &nums2)
    {
        int bIsOdd = 0;
        int medianIndex = 0;

        if ((nums1.size() + nums2.size()) % 2 == 0)
            bIsOdd = 0;
        else
            bIsOdd = 1;

        medianIndex = (nums1.size() + nums2.size()) / 2;

        vector<int> v(medianIndex + 1);

        for (int i = 0; i < medianIndex + 1; i++)
        {
            if (!nums1.empty() && !nums2.empty())
            {
                if (nums1[0] >= nums2[0])
                {
                    v[i] = nums2[0];
                    nums2.erase(nums2.begin());
                }
                else
                {
                    v[i] = nums1[0];
                    nums1.erase(nums1.begin());
                }
            }
            else
            {
                if (nums1.empty())
                {
                    v[i] = nums2[0];
                    nums2.erase(nums2.begin());
                }
                else
                {
                    v[i] = nums1[0];
                    nums1.erase(nums1.begin());
                }
            }
        }

        if (bIsOdd)
            return v[v.size() - 1];
        else
        {
            double temp = v.back();
            v.pop_back();
            return (double)(temp + v.back()) / 2;
        }
    }
};