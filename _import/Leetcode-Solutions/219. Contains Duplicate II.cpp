class Solution {
public:
    bool containsNearbyDuplicate(vector<int>& nums, int k) {
        unordered_set<int>mp;
        for(int i=0;i<nums.size();i++){
            if(mp.count(nums[i])) return true;
            mp.insert(nums[i]);
            if(mp.size()>k){
                mp.erase(nums[i-k]);
            }
            
        }
        return false;
    }
};
