// Created by sjyan @2017年3月25日
// Time Complexity: O(n)    Space Complexity: O(1)

class Solution {
public:
    vector<string> findWords(vector<string>& words) {
        char row0[] = "qwertyuiop";     // size == 10
        char row1[] = "asdfghjkl";      // size == 9
        char row2[] = "zxcvbnm";        // size == 7
        
        vector<string> result;
    
        for (vector<string>::iterator it = words.begin(); it != words.end(); it++)
        {
            int flag_row = -1;  // 0: in row0    1: in row1    2: in row2
            int flag_diffrow = 0;    // 0: same row   1: different row
            string str = *it;
            int length = str.size();
    
            if(length == 1) result.push_back(str);
            else
            {
                char first = str[0];
    
                // check row0
                for(int i=0; i<10; i++)
                {
                    if(first == row0[i] | (first+32) == row0[i])
                    {
                        flag_row = 0;
                        break;
                    }
                }
    
                // check row1
                if(flag_row == -1)
                {
                    for(int i=0; i<9; i++)
                    {
                        if(first == row1[i] | (first+32) == row1[i])
                        {
                            flag_row = 1;
                            break;
                        }
                    }
                }
                
                // check row2
                if(flag_row == -1)
                {
                    for(int i=0; i<7; i++)
                    {
                        if(first == row2[i] | (first+32) == row2[i])
                        {
                            flag_row = 2;
                            break;
                        }
                    }
                }
    
                switch(flag_row)
                {
                    case 0:
    
                    // scan str
                    for(int i=1; i<length; i++)
                    {
                        char c = str[i];
                        int flag_in = 0;
                        
                        // check row0
                        for(int j=0; j<10; j++)
                        {
                            if(c == row0[j] | (c+32) == row0[j])
                            {
                                flag_in = 1;
                                break;
                            }
                        }
    
                        if(flag_in) continue;
                        else
                        {
                            flag_diffrow = 1;
                            break;
                        }
                    }
    
                    if(flag_diffrow == 0)   result.push_back(str);
    
                    break;
    
                    case 1:
    
                    // scan str
                    for(int i=1; i<length; i++)
                    {
                        char c = str[i];
                        int flag_in = 0;
                        
                        // check row1
                        for(int j=0; j<9; j++)
                        {
                            if(c == row1[j] | (c+32) == row1[j])
                            {
                                flag_in = 1;
                                break;
                            }
                        }
    
                        if(flag_in) continue;
                        else
                        {
                            flag_diffrow = 1;
                            break;
                        }
                    }
    
                    if(flag_diffrow == 0)   result.push_back(str);
    
                    break;
    
                    case 2:
                    
                    // scan str
                    for(int i=1; i<length; i++)
                    {
                        char c = str[i];
                        int flag_in = 0;
                        
                        // check row2
                        for(int j=0; j<7; j++)
                        {
                            if(c == row2[j] | (c+32) == row2[j])
                            {
                                flag_in = 1;
                                break;
                            }
                        }
    
                        if(flag_in) continue;
                        else
                        {
                            flag_diffrow = 1;
                            break;
                        }
                    }
    
                    if(flag_diffrow == 0)   result.push_back(str);
    
                    break;
                }
            }
        }
        
        return result;
    }
};