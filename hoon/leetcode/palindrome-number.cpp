#include <iostream>
using namespace std;

int square(int num)
{
    int tmp = 1;
    if (num!=0)
        for(int i=0; i<num; i++)
            tmp *= 10;
    else
        tmp = 1;

    return tmp;
}

bool isPalindrome(int x) {
    cout << x << endl;
    
    int temp = x;
    if (x < 0)
        return false;
    else if(x < 10)
        return true;

    // get length of x
    int len = 1;
    while (temp / 10 != 0)
    {   
        len++;
        temp /= 10;
    }
    
    int index = 1;
    while (len - index >= 1)
    {
        if(index == 1)
        {
            if (x / square(len-1) == x % square(index))
            {
                x = x % square(len-1) / square(index);
                len-=2;
            }
            else
            {
                return false;
            }
        }
        else
        {
            if (x / square(len-1) == x / square(index))
            {
                x = x % square(len-1) / square(index);
                len--;
            }
            else
            {
                return false;
            } 
        }
    };

    return true;
}

int main()
{
    int x = 1123211;
    cout << isPalindrome(x) << endl;
    return 0;
}