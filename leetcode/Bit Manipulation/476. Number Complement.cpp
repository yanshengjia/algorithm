// Created by sjyan @2017年3月25日
// Time Complexity: O(lgN)    Space Complexity: O(1)

class Solution {
public:
    int findComplement(int num) {
        int array[32];
        int counter = 31;
        int head_position = 0;
        int num_length = 0;
        int complement_number = 0;

        for(int i=0; i<32; i++)
        {
            array[i] = 0;
        }

        // convert num to binary representation
        if(num == 1)    array[31] = 1;
        else if(num >= 2)
        {
            while(num/2 != 0)
            {
                if(num%2 == 1)    array[counter] = 1;
                num /= 2;
                counter--;
            }
            array[counter] = 1;
        }

        for(int i=0; i<32; i++)
        {
            if(array[i] == 1)
            {
                head_position = i;
                break;
            }
        }

        // get the complement number
        num_length = 32 - head_position;
        int complement[num_length];

        for(int i=0; i<num_length; i++)
        {
            complement[i] = 1 - array[head_position + i];
        }

        for(int i=0; i<num_length; i++)
        {
            complement_number += complement[num_length-i-1]*pow(2,i);
        }

        return complement_number;
    }
};
