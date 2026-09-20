/*
 * DSA Lesson · H1
 *
 * Pattern : Data Structures & Algorithms
 * Written : 26 Jun 2026
 * Time    : O(n)
 * Space   : O(1)
 */

/*#include <iostream>
#include <unordered_map>
#include <vector>
using namespace std;

class hashtable {
    vector<int> table;
    int tsize;

public:
    hashtable(int size) {
        tsize = size;
        table.resize(size, -1);
    }

    int hashfunc(int key) {
        return key % tsize;
    }

    void insertkey(int key) {
        int index = hashfunc(key);
        table[index].push_back(key);
        while (table[index] != -1) {
            index = (index + 1) % tsize;
        }
        table[index]=key;
    }

    void display() {
        for (int i = 0; i < tsize; i++) {
            cout << i << ": ";
            if (table[i] == -1)
                cout << "empty";
            else
                cout << table[i];
            cout << "\n";
        }
    }


    void freq(int key) {
        int n = key;
        unordered_map<int, int> freqq;
        for (int i = 0; i < tsize; i++) {
            for (int x: table[i]) {
                freqq[x]++;
            }
        }
        for (auto &o: freqq) {
            cout << o.first << " appears " << o.second << " times." << endl;
        }
    }
};

int main() {
    hashtable ht(7);
    ht.insertkey(10);
    ht.insertkey(13);
    ht.insertkey(12);
    ht.insertkey(20);
    ht.insertkey(20);
    ht.display();

}
*/

/*#include <iostream>
#include <vector>
#include<functional>
#include <list>
#include <utility>
#include <string>
using namespace std;

template<typename key,typename value>
class hashtable {
    vector<list<pair<key,value>>>table;
    int tsize;
public :
    hashtable(int size=7) {
    tsize=size;
    table.resize(size);

}
    unsigned hashfunc(const key &k) {
    return hash<key>()(k) % tsize;
}
    void insert(const key &k,const value &v) {
    unsigned index= hashfunc(k);

    for (auto &p : table[index]) {
        if (p.first==k) {
            p.second=v;

            return;
        }
    }
    table[index].push_back({k,v});
}
    void times(const key &k) {
    int t=0;
    for (auto &p:table) {
        for (auto &x : p) {
            if (x.first==k) {
                t++;
            }
        }
    }
    cout<<k<<" appears "<<t<<" times "<<endl;
}
    void display() {
    int index=0;
    for (auto &p:table) {

        cout << "index " << index << ": ";
        for (auto &q : p) {
            cout<<q.first<<"->"<<q.second<<" "<<endl;
        }
        cout<<endl;
        index++;

    }
}
    void search(const key &k){
        unsigned index=hashfunc(k);
        for (auto &p:table[index]) {
            if (p.first==k) {
                cout<<p.second<<endl;
                return;
            }
        }
        cout<<"not found"<<endl;;
    }
    void remove(const key &k){
        int index=hashfunc(k);
        for (auto it = table[index].begin();it!=table[index].end();it++){
            if (it->first==k) {
                table[index].erase(it);
                cout<<"deleted"<<endl;
                return;
            }
        }
        cout<<"Not found"<<endl;
    }
    /*void maximumcount() {
    string a="";
    vector<list<pair<int,int>>>maxi;
    for (auto &i:table) {
        for (auto &p:i) {
            a+=p.first;
            for (char c:a) {
                if (isdigit(c)) {
                    unsigned index = hashfunc(c);
                    maxi[index]=c;
                }

            }
            a.clear();
        }
    }

}
};


int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    hashtable<string,int>hs;
    hashtable<int,int>hi;
    hashtable<float,int>hf;
    hs.insert("yash",20);
    hi.insert(2005,2025);
    hi.insert(1,2);
    hi.insert(1,3);
    hi.insert(1,4);
    hi.insert(2,1);
    hi.insert(2,3);
    hf.insert(5.9,6);

    hi.display();


    hi.search(2005);
    hi.search(2006);
    hi.remove(2005);
    hi.times(1);
}*/
/*#include <iostream>
#include <unordered_map>
using namespace std;
int main() {
    unordered_map<int,int>a;
    a[2]=100;
    a[3]=200;
    a[4]=300;
    if (a.count(2)) {
        cout<<a[2];
    }
    for (auto &x:a) {
        a[x]++;
    }
    for (auto &x:a) {
    }
}*/
/*#include <iostream>
#include <vector>
#include<list>
#include <utility>
using namespace std;
template<typename key,typename value>
class hashtable{
    vector<list<pair<key,value>>>table;
    vector<list<pair<key,value>>>ntable;
    size_t table_size;

public:
    hashtable(size_t size) {
        table_size=size;
        table.resize(table_size);
    }
    size_t hashf(const key &k) {
        return (k*31)%table_size;
    }
    void insert(const key &k, const value &v) {
        size_t index=hashf(k);
        for (auto& c: table[index]) {

                if (c.first==k) {
                    c.second=v;
                    return;
                }


        }
        return table[index].push_back({k,v});

    }
    void display() {
        int x=0;
        for (auto& c: table) {

            for (auto&d : c) {
                cout<<x<<": "<<d.first<<" ->"<<d.second<<endl;
            }
            x++;

        }
    }
    void remove(const key &k,const value &v){
        size_t index=hashf(k);
        for (auto it = table[index].begin(); it != table[index].end(); ++it) {
            if (it->first == k && it->second == v) {
                table[index].erase(it);
                break;
            }
        }

    }
    void rehash() {

        table_size=table_size*2;
        ntable.resize(table_size);
        for (auto&c :table) {
            for (auto& d:c) {
                size_t h=hashf(d.first);

                    ntable[h].push_back({d.first,d.second});


            }
        }
        int x=0;
        for (auto& c: ntable) {

            for (auto&d : c) {
                cout<<x<<": "<<d.first<<" ->"<<d.second<<endl;
            }
            x++;

        }

    }

};
int main() {
    hashtable<int,string> obj(7);
    obj.insert(2,"hi");
    obj.insert(3,"hii");
    obj.insert(4,"hiii");
    obj.insert(5,"hiiii");
    obj.insert(6,"hiiiii");
    obj.insert(7,"hiiiiii");
    obj.insert(8,"hiiiiiii");
    obj.insert(9,"hiiiiiiii");

    //obj.display();
    //obj.remove(2,"hii");
    //cout<<"after delete"<<endl;
    obj.display();
    cout<<"after reshashing"<<endl;
    obj.rehash();
}*/
/*#include <iostream>
using namespace std;
int main() {
    int x=10;
    int *p=&x;
    int **w=&p;
    cout<<x<<" "<<*p<<" "<<**w<<" "<<&p<<" "<<&w;
}*/
/*#include <iostream>
#include <bitset>
using namespace std;
int main() {
    int x=5;
    int y=10;
    cout<<bitset<4>(x)<<endl;
    cout<<bitset<4>(y)<<'\n';
    cout<<bitset<5>(x^y)<<'\n';
    if (!(x^y)) {
            cout<<"yes\n";
    }
    else {
        cout<<"no\n";
    }
    cout<<(x|y)<<'\n';
    cout<<(x&y)<<'\n';
    cout<<bitset<5>(x<<1)<<'\n';
    cout<<bitset<5>(x>>1)<<'\n';
    cout<<(x<<1)<<" == "<<(x*2);

return 0;

}*/
/*#include <iostream>
#include <vector>
#include <utility>
#include<list>
using namespace std;
template<typename key,typename value>
class hashtable {
    vector<list<pair<key,value>>> table;
    size_t s=8;


public:
    hashtable(size_t s) {
        table.resize(s);
        state.resize(s,0);
    }
    size_t hashf(const key &k) {
        size_t index = hash<key>{}(k)% s;
        return index;
    }
    void insert( const key &k, const value &v) {
        size_t index = hashf(k);
        while (state[index]==1 || state[index]==2){

                index=(index+1)%s;

        }
        for (auto &m:  table[index]) {
            if (m.first==0) {
                m.first=1;
                m.second=1;
                table[index].push_back({k,v});
            }
            else {
                index=(index+1)%s;
            }
        }
        table[index].push_back({1,1});
        table[index].push_back({k,v});


    }
    void display() {
        int index=0;
        for (auto &k:table) {
            cout<<index<<"->";
            for (auto &m:k) {
                cout<<m.first<<' '<<m.second<<'\n';
            }



            index++;
        }
    }


};
int main() {
    hashtable<int,int> obj(8);
    obj.insert(10,20);
    obj.insert(20,40);
    obj.insert(30,60);
    obj.insert(40,80);
    obj.display();
}*/
/*#include <iostream>
#include <vector>
using namespace std;
int main() {
    vector<int>arr(3);
    arr[0]=31;
    arr[1]=32;
    arr[2]=33;

    int q=*(arr.data()+1);
    cout<<q;
    cout<<sizeof(int);

}*/
/*#include <vector>
#include <iostream>
using namespace std;
int main() {
    vector <int> arr;
    //arr.resize(5);
    arr.push_back(4);
    arr.push_back(8);
    arr.push_back(12);
    arr.push_back(16);
    arr.push_back(20);
    cout<<"array:\n";

    for (auto &m:arr) {
        cout<<m<<' ';

    }
    cout<<'\n';
    int s=arr.size();
    cout<<"reverse array: \n";
    for (int i=s-1;i>=0;i--) {
        cout<<arr[i]<<' ';
    }

}*/
/*#include <iostream>
#include <unordered_map>
using namespace std;
int main() {
    unordered_map<int,int> mp;
    mp[1]=10;
    cout<<mp[1];
}*/
/*#include <iostream>
#include <unordered_map>
#include <vector>
using namespace std;
int main() {
    string s="leetcode";
    unordered_map<char,int>freq;
    vector<char> store;

    for (auto &c :s) {
        freq[c]++;
    }
    for (auto it=freq.begin();it!=freq.end();it++) {
        if (it->second==1) {
            cout<<it->first<<' '<<freq.bucket(it->first)<<'\n';
            break;
        }
    }
    cout<<"Frequency:\n";
    for (auto it=freq.begin();it!=freq.end();it++) {
        cout<<it->first<<' '<<it->second<<' '<<freq.bucket(it->first)<<'\n';
    }
    for (auto &c : s) {
        store.push_back(c);
    }
    cout<<"index of string\n";
    int si=size(store);
    for (int i=0;i<si;i++) {
        cout<<store[i]<<' '<<i<<'\n';
    }

    cout<<"Rockkie\n";
    for (int i=0;i<si;i++) {
        cout<<store[i]<<' '<<freq[store[i]]<<'\n';
    }
}*/
/*#include <iostream>
#include <unordered_map>
using namespace std;
int main() {
    unordered_map<int,int>m;
    for (int i=0;i<5;i++) {
        m[i];
    }
    cout<<m[1];
}*/
/*#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;
class Solution {
public:
    int sc(vector<int>&nums,int n){
        int pres=0;
        for(int i=0;i<=n;i++){
            pres=pres+nums[i];
        }
        int mi=nums[n+1];

        for(int i=2;n+i<nums.size();i++){
            mi=min(mi,nums[n+i]);
        }
        int s=pres-mi;
        return s;

    }
    long long maximumScore(vector<int>& nums) {
        int si=nums.size();
        int maxi=sc(nums,0);
        for(int i=0;i<si-1;i++){
            maxi=max(maxi,sc(nums,i));
        }
        return maxi;
    }
};
int main() {
    int n;
    cin >> n;

    vector<int> nums(n);

    for(int i = 0; i < n; i++) {
        cin >> nums[i];
    }
    Solution ans;
    int a= ans.maximumScore(nums);
    cout<<a;
}*/
#include <iostream>
#include <unordered_map>
#include <unordered_set>
#include <string>
using namespace std;
int main() {
    unordered_multimap<int,string>me;
    me.insert({12306974,"Yogender"});
    me.insert({12306974,"21"});
    me.insert({12306974,"His soulmate:- Yuvika"});
    auto range=me.equal_range(12306974);
    for (auto it=range.first;it!=range.second;it++) {
        cout<<it->first<<" "<<it->second<<endl;
    }

}
