class Solution {
public:
    vector<int> sortArrayByParity(vector<int>& A) {
        vector<int> out(A.size(),0);
        int x(0), y(A.size()-1);
        for(int i=0;i<A.size();i++){
            if( A[i] % 2 ){
                out[y] = A[i];
                y--;
            }
            else{
                out[x] = A[i];
                x++;
            }
        }
        return out;
    }
};