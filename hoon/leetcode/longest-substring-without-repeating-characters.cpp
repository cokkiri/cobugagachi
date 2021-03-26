#include <iostream>
#include <string>
using namespace std;
class Solution
{
public:
    int lengthOfLongestSubstring(string s)
    {
        string substring = "";
        string currentsSubstring = "";
        for (int i = 0; i < s.size(); i++)
        {
            int j = 0;
            for (j = 0; j < currentsSubstring.size(); j++)
            {
                if (currentsSubstring[j] == s[i])
                {
                    if (substring.size() < currentsSubstring.size())
                        substring = currentsSubstring;

                    break;
                }
            }

            if (j < currentsSubstring.size())
            {
                currentsSubstring = currentsSubstring.substr(j + 1, currentsSubstring.size()) + s[i];
            }
            else
            {
                currentsSubstring += s[i];
            }
        }

        if (substring.size() < currentsSubstring.size())
            substring = currentsSubstring;

        return substring.size();
    }
};