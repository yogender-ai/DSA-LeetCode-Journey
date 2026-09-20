/*
 * LeetCode 50 · Pow(x, n) · Medium
 * https://leetcode.com/problems/powx-n/
 *
 * Pattern : Math & Logic
 * Solved  : 03 Feb 2026
 * Time    : O(n)
 * Space   : O(1)
 */

class Solution {
public:
    double pow(double x,long long n,double w){
        if(n==0) return w;
        return pow(x,n-1,w*x);
    }
    double p(double x,long long n,double w){
        if(n==0) return w;
        return (p(x,n+1,w*x));
    }
    double myPow(double x, long long  n) {
        if(n==0) return 1;
        if(x==1) return 1;
        if(x== -1 ){

            if(n%2!=0){
                return -1;
            }
            else return 1;
        }
        if(n>0){
            double r=pow(x,n/2,1);
            if(n % 2 == 0)
                return r * r;
            else
                return r * r * x;   
        }
        else{
            double rr= p(x,n/2,1);
            if(n % 2 == 0)
                return 1/(rr * rr);
            else
                return 1/(rr * rr * x);   

        }
        
        
        
    }
};
