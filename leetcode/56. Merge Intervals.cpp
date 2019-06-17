// Author: Shengjia Yan
// Date: 2018-05-11 Friday
// Email: i@yanshengjia.com
// Time Complexity: O(n)
// Space Complexity: O(n)

/**
 * Definition for an interval.
 * struct Interval {
 *     int start;
 *     int end;
 *     Interval() : start(0), end(0) {}
 *     Interval(int s, int e) : start(s), end(e) {}
 * };
 */
class Solution {
public:
    static bool my_compare(const Interval &a, const Interval &b)
    {
        return a.start < b.start;
    }
    
    vector<Interval> merge(vector<Interval>& intervals) {
        int length = intervals.size();
        vector<Interval> res;
        
        sort(intervals.begin(), intervals.end(), my_compare);
        
        for(int i=0; i<length; i++) {
            if (res.empty())
                res.push_back(intervals[i]);
            else {
                int size = res.size();
                if (res[size-1].start <= intervals[i].start && intervals[i].start <= res[size-1].end) {
                    int max = intervals[i].end > res[size-1].end ? intervals[i].end : res[size-1].end;
                    res[size-1].end = max;
                }
                else {
                    res.push_back(intervals[i]);
                }
            }
        }
        return res;
    }
};