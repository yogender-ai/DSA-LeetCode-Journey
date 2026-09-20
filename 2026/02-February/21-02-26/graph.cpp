/*
 * DSA Lesson · Graph
 *
 * Pattern : Data Structures & Algorithms
 * Written : 21 Feb 2026
 * Time    : O(n)
 * Space   : O(1)
 */

#include <iostream>
#include <vector>
using namespace std;

/*
   Graph:
   1-2-3-6
   | |/|
   0 7 4-5
*/

int main() {

    // 0..7 -> total 8 nodes
    vector<vector<int>> adj(8);

    // add edges (undirected)
    adj[1].push_back(2);
    adj[2].push_back(1);

    adj[2].push_back(3);
    adj[3].push_back(2);

    adj[3].push_back(6);
    adj[6].push_back(3);

    adj[1].push_back(0);
    adj[0].push_back(1);

    adj[2].push_back(7);
    adj[7].push_back(2);

    adj[3].push_back(7);
    adj[7].push_back(3);

    adj[3].push_back(4);
    adj[4].push_back(3);

    adj[4].push_back(5);
    adj[5].push_back(4);


    for(int i = 0; i < adj.size(); i++){
        cout << i << " -> ";
        for(int x : adj[i]) cout << x << " ";
        cout << endl;
    }
}
