#include <iostream>
#include <string>
using namespace std;

long long square(int num)
{
    int tmp = 1;
    if (num!=0)
        for(int i=0; i<num; i++)
            tmp = 10 * tmp;
    else
        tmp = 1;

    return tmp;
}

int myAtoi(string s) {
    // -1: negative, 1: positive, 0: not mentioned
    int bSign = 0;
    int numIndex = -1;

    // find first number index and sign
    for (int i=0; i<s.size(); i++)
    {
        int numVal = int(s[i]);
        if (numVal == 32)
            continue;

        if (numVal == 45 || numVal == 43) // 45(-)
        {
            bSign = (numVal == 45) ? -1 : 1;
            if (i+1 < s.size())
            {
                if(int(s[i+1]) >= 48 && int(s[i+1]) <= 57)
                {
                    numIndex = i+1;
                    break;
                }
                else
                {
                    return 0;
                }
            }
        }

        // ascii code 48(0) ~ 57(9)
        if (numVal >= 48 && numVal <= 57)
        {
            numIndex = i;
            break;
        }
        else
        {
            return 0;
        }
    }

    // if number doesn't exist
    if (numIndex == -1)
        return 0;

    // remove front 0
    while(int(s[numIndex]) == 48)
        numIndex++;

    // +-12 => return 0;
    if (!(48 <= int(s[numIndex]) && int(s[numIndex]) <= 57))
        return 0;

    // read number
    char numberArr[10] = {0,};
    int i; // length of real number
    for(i=0; (48 <= int(s[numIndex]) && int(s[numIndex]) <= 57) && i<10; i++, numIndex++)
    {
        numberArr[i] = s[numIndex];
    }

    if ((48 <= int(s[numIndex]) && int(s[numIndex]) <= 57) && numIndex < s.size())
    {
        if (bSign >= 0)
            return INT_MAX;
        else
            return INT_MIN;
    }

    long long number = 0;
    for(int j=0; j<i; j++)
        number += (int(numberArr[j])-48) * square(i-j-1);

    if (number >= INT_MAX && bSign >= 0)
        return INT_MAX;
    else if((-1)*number <= INT_MIN && bSign == -1)
        return INT_MIN;

    if (bSign >= 0)
        return (int)number;
    else 
        return (int)(-1)*number;
}

int main()
{
    // string s = "42";
    // string s = "words and 987";
    // string s ="   -42";
    // string s = "-91283472332";
    // string s = "+-12";
    // string s = "00000-42a1234";
    // string s = "  0000000000012345678";
    // string s = "-000000000000001";
    // string s = "-6147483648";
    string s = "    -88827   5655  U";

    cout << myAtoi(s) << endl;
    return 0;
}