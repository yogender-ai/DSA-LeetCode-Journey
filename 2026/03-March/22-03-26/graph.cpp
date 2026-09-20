/*
 * DSA Lesson · Graph
 *
 * Pattern : Data Structures & Algorithms
 * Written : 22 Mar 2026
 * Time    : O(n)
 * Space   : O(1)
 */

#include <iostream>
#include <vector>
#include <list>
using namespace std;

class graph {
    vector<list<int>> adj;

public:
    graph(int v) {
        adj.resize(v);
    }

    void insert(int u, int v) {
        adj[u].push_back(v);
        adj[v].push_back(u); // remove if directed
    }

    void display() {
        for (int i = 0; i < adj.size(); i++) {
            cout << i << " -> ";
            for (int x : adj[i]) {
                cout << x << " ";
            }
            cout << endl;
        }
    }
};

int main() {
    graph g(4);

    g.insert(0, 1);
    g.insert(1, 2);
    g.insert(1, 3);

    g.display();
}
