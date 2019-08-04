// Created by sjyan @2017-02-05
// Time Complexity: O(lgN)
// Space Complexity: O(1)

class Solution {
public:
    int hammingDistance(int x, int y) {
        int array_x[32];
        int array_y[32];
        int hamming_distance = 0;

        for(int i=0; i<32; i++)
        {
            array_x[i] = 0;
            array_y[i] = 0;
        }

        // convert x to binary
        int x_counter = 31;

        if(x == 1)  array_x[31] = 1;
        else if(x >= 2)
        {
            while(x/2 != 0)
            {
                if(x%2 == 1)    array_x[x_counter] = 1;

                x /= 2;
                x_counter--;
            }
            array_x[x_counter] = 1;
        }

        // convert y to binary
        int y_counter = 31;

        if(y == 1)  array_y[31] = 1;
        else if(y >= 2)
        {
            while(y/2 != 0)
            {
                if(y%2 == 1)    array_y[y_counter] = 1;

                y /= 2;
                y_counter--;
            }
            array_y[y_counter] = 1;
        }


        for(int i=0; i<32; i++)
        {
            if(array_x[i] != array_y[i])
                hamming_distance++;
        }

        return hamming_distance;
    }
};
