#include <iostream>
using namespace std;
#include <map>


# Map
class MyCalendar {
public:
    MyCalendar() {}
    
    bool book(int start, int end) {
        auto it = cal.lower_bound(start);
        if (it != cal.end() && it->first < end) return false;
        if (it != cal.begin() && prev(it)->second > start) return false;
        cal[start] = end;
        return true;
    }

private:
    map<int, int> cal;
};