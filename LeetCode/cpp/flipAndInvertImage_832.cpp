class Solution {
public:
    vector<vector<int>> flipAndInvertImage(vector<vector<int>>& A) {
        vector<vector<int>> out(A.size(),vector<int> (A[0].size()) );
        for(int i=0; i<A.size(); i++){
            for(int j=0; j<A[0].size(); j++){
                out[i][ A[0].size()-1-j ] = 1 - A[i][j];
            }
        }
        return out;
    }
};