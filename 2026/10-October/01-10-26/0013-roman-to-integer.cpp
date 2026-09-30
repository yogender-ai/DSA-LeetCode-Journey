/*
 * LeetCode 13 · Roman to Integer · Easy
 * https://leetcode.com/problems/roman-to-integer/
 *
 * Pattern : Arrays & Hashing
 * Solved  : 1 Oct 2026
 * Time    : O(n) · Runtime: 0 ms (Beats 100.0%)
 * Space   : O(1) · Memory: 10.1 MB (Beats 76.3%)
 */

class Solution {
public:
    int romanToInt(string s) {
        int temp=0;
        for(int i=0;i<s.size();i++ ){
            if(s[i]=='I'){
                if(s[i]=='I'&& s[i+1]=='V'){
                    temp+=4;
                    i+=1;
                }
                else if(s[i]=='I'&& s[i+1]=='X'){
                    temp+=9;
                    i+=1;
                }
                else{
                    temp+=1;
                }
            }
            else if(s[i]=='V'){
                temp+=5;
            }
            else if (s[i]=='X'){
                if(s[i]=='X'&& s[i+1]=='L'){
                    temp+=40;
                    i+=1;
                }
                else if (s[i]=='X'&&s[i+1]=='C'){
                    temp+=90;
                    i+=1;
                }
                else temp+=10;

            }
            else if(s[i]=='L'){
                temp+=50;
            }
            else if (s[i]=='C'){
                if(s[i]=='C'&& s[i+1]=='D'){
                    temp+=400;
                    i+=1;
                }
                else if (s[i]=='C'&&s[i+1]=='M'){
                    temp+=900;
                    i+=1;
                }
                else temp+=100;

            }
            else if(s[i]=='D'){
                temp+=500;
            }else if(s[i]=='M'){
                temp+=1000;
            }
            
            

        }
        return temp;
        
    }
};
