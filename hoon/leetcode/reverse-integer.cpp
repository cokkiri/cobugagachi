class Solution {
public:
    int square(int num)
    {
        int tmp = 1;
        if (num!=0)
            for(int i=0; i<num; i++)
                tmp = 10 * tmp;
        else
            tmp = 1;
    
        return tmp;
    }
    
    int reverse(int x) {
        int input_x = x;
        int counter = 0;
        int tmp = 0;
        if (x==0 || x >= INT_MAX || x <= INT_MIN)
            return 0;
        
        while (input_x/10 != 0)
        {
            counter++;
            input_x /= 10;
        }

        while (x/10 != 0)
        {
            if (tmp + (long long)x % 10 * square(counter) >= INT_MAX || tmp + (long long)x % 10 * square(counter) <= INT_MIN)
                return 0;
            tmp += x % 10 * square(counter);
            counter--;
            x /= 10;
        }
        tmp += x % 10;
        return tmp;
        
    }
};