class Solution {
public:
    int heightChecker(vector<int>& heights) {
        vector<int> heights2 = heights;
        sort(heights2.begin(),heights2.end());
        int total = 0;
        for(int i=0;i<heights2.size();i++){
            if(heights2[i] != heights[i]){
                total += 1;
            }
        }
        return total;
    }
};