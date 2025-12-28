class Solution {
public:
    long long maximumScore(vector<int>& nums) {
        long long  si=nums.size();
        vector<long long>pref(si);
        vector<long long>sufm(si);
        pref[0]=nums[0];
        for(long long i=1;i<si;i++){
            pref[i]=pref[i-1]+nums[i];
        }
        sufm[si-1]=nums[si-1];
        for(long long i=si-2;i>=0;i--){
            sufm[i]=min<long long>(nums[i],sufm[i+1]);
        }
        long long ans=LLONG_MIN;
        for(long long i=0;i<si-1;i++){
            ans=max(ans,pref[i]-sufm[i+1]);
        }
        return ans;
        
    }
};
