class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_set<int> st; // Unordered Set
        for(auto &x :nums){
            if(st.count(x)) { // Duplicate Found
                return true ;
            }
            st.insert(x); // Duplicate Not Found! Inserting in Set
        }
        return false;
    }
};