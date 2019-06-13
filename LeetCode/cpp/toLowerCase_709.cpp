class Solution {
public:
    string toLowerCase(string str) {
        for (auto it = str.begin(); it!=str.end(); it++) {
            if (*it <= 'Z' && *it >= 'A') {
                *it = lower(*it);
            }
        }
        return str;
    }
    char lower(char s) {
        return s - ('Z' - 'z');
    }
};