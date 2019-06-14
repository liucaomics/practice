class Solution {
public:
    /*
    vector<int> sortedSquares(vector<int>& A) {
        vector<int> out(A.size());
        for(int i=0;i<A.size();i++){
            out[i] = A[i]*A[i];
        }
        quickSort(out,0,out.size()-1);
        return out;
    }
    
    void quickSort(vector<int>& A, int low, int high){
        if(low < high){
            int pilot = partition(A, low, high);
            quickSort(A, low, pilot-1);
            quickSort(A, pilot+1, high);
        }
    }
    
    int partition(vector<int>& A, int low, int high){
        int pilot = A[low]; // randomly select a pilot
        int i = low; // the index separate smaller and larger values
        for(int j=low+1; j<=high; j++){
            if(A[j]<=pilot){
                swap(&A[j],&A[++i]);
            }
        }
        swap(&A[low], &A[i]);
        return i;
    }
    
    void swap(int* a, int* b){
        int temp = *a;
        *a = *b;
        *b = temp;
    }*/
    vector<int> sortedSquares(vector<int>& A) {
        vector<int> out(A.size());
        int low=0, high=A.size()-1, i = A.size()-1;
        while(i>=0){
            out[i] = abs(A[low])>=abs(A[high])?pow(A[low++],2):pow(A[high--],2);
            i--;
        }
        
        return out;
    }
};