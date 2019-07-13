#include<stack>

class Solution {
public:
    string removeOuterParentheses(string S) {
        stack<char> sta;
        int start(0), end(0);
        string output;
        for(int i=0;i<S.size();i++){
            if(!sta.empty()){
                if( sta.top() == '(' && S[i] == ')' ){
                    sta.pop();
                    if(sta.empty()){
                        end = i;
                        output.append(S.substr(start+1,end-start-1));
                        start = end + 1;
                    }
                }
                else{
                    sta.push(S[i]);
                }
            }
            else{
                sta.push(S[i]);
            }
        }
        return output;
    }
};


