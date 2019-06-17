// created by sjyan @2016-11-10
// Time Complexity: O(n)    Space Complexity: O(1)

class Solution {
public:
  char findTheDifference(string s, string t) {
    int vs = 0;
    int vt = 0;

    for (int i = 0; i < s.size(); i++)
      vs += s[i];

    for (int j = 0; j < t.size(); j++)
      vt += t[j];

    char res = vt - vs;

    return res;
  }
};
