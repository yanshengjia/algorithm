// Author: Shengjia Yan
// Date: 2017年7月1日
// Email: sjyan@seu.edu.cn
// Time Complexity: O(n)
// Space Complexity: O(1)


class Rectangle {
    /*
     * Define two public attributes width and height of type int.
     */
    // write your code here

    /*
     * Define a constructor which expects two parameters width and height here.
     */
    // write your code here
    
    /*
     * Define a public method `getArea` which can calculate the area of the
     * rectangle and return.
     */
    // write your code here
public:
    int width;
    int height;
    
    Rectangle(int w, int h) {
        width = w;
        height = h;
    }
    
    int getArea() {
        return width*height;
    }
};
