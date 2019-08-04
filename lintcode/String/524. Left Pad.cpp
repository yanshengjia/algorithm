// Author: Shengjia Yan
// Date: 2017年7月24日
// Email: sjyan@seu.edu.cn


class StringUtils {
public:
    /**
     * @param originalStr the string we want to append to
     * @param size the target length of the string
     * @param padChar the character to pad to the left side of the string
     * @return a string
     */
    static string leftPad(string& originalStr, int size, char padChar=' ') {
        // Write your code hered
        int length = originalStr.length();
        
        if (length == size) return originalStr;
        else {
            int left_size = size - length;
            string res = "";
            
            for (int i=0; i<left_size; i++) {
                res += padChar;
            }
            
            res += originalStr;
            return res;
        }
    }
};