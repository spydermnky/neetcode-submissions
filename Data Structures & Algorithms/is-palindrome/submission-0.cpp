class Solution {
public:
    bool isPalindrome(string s) {
        string processed = "";
        for (char c : s){
            if (isalnum(c)){
                processed += tolower(c);
            }
        }
        for (int i = 0, j = processed.length() - 1; i < j; ++i, --j){
            if (processed[i] != processed[j]){
                return false;
            }
        }
        return true;
    }
};
