#include <iostream>
#include <string>

using namespace std;

class Solution
{
public:
    string convert(string s, int numRows)
    {
        if (numRows == 1 || s.size() == 1 || s.size() < numRows)
            return s;

        string result = "";
        for (int i = 0; i < numRows; i++)
        {
            int counter = 0;
            int tmp = i;
            do
            {
                result += s[tmp];
                // cout << result << '\t' << tmp << endl;
                if (i == 0 || i == numRows - 1)
                {
                    tmp += (numRows - 1) * 2;
                }
                else
                {
                    if (counter % 2 == 0)
                        tmp += (numRows - (i + 1)) * 2;
                    else
                        tmp += 2 * i;
                    counter++;
                }
            } while (tmp < s.size());
        }

        return result;
    }
};