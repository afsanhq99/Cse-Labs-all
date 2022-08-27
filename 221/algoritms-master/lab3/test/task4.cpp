#include <bits/stdc++.h>
using namespace std;

void add_edge(vector<int> adj[], int src, int dest)
{
    adj[src].push_back(dest);
    adj[dest].push_back(src);
}

bool BFS(vector<int> adj[], int src, int dest, int v,
         int pred[], int dist[])
{
 //edike first e sob node e false
    list<int> queue;
    bool visited[v];
    for (int i = 0; i < v; i++)
    {
        visited[i] = false;
        dist[i] = INT_MAX;
        pred[i] = -1;
    }
    visited[src] = true;
    dist[src] = 0;
    queue.push_back(src);

    // standard BFS algorithm
    while (!queue.empty())
    {
        int u = queue.front();
        queue.pop_front();
        for (int i = 0; i < adj[u].size(); i++)
        {
            if (visited[adj[u][i]] == false)
            {
                visited[adj[u][i]] = true;
                dist[adj[u][i]] = dist[u] + 1;
                pred[adj[u][i]] = u;
                queue.push_back(adj[u][i]);

                // We stop BFS when we find
                // destination.
                if (adj[u][i] == dest)
                    return true;
            }
        }
    }

    return false;
}

void printShortestDistance(vector<int> adj[], int s,
                           int dest, int v)
{

    int pred[v], dist[v];

    if (BFS(adj, s, dest, v, pred, dist) == false)
    {
        cout << "Given source and destination"
             << " are not connected";
        return;
    }
    vector<int> path;
    int crawl = dest;
    path.push_back(crawl);
    while (pred[crawl] != -1)
    {
        path.push_back(pred[crawl]);
        crawl = pred[crawl];
    }
    cout << "Minimum number of bridges are : "
         << dist[dest];
}

int main()
{
    int T;
    cin >> T;
    for (int i = 0; i < T; i++)
    {
        int ver, edg;
        cin >> ver >> edg;

        vector<int> adj[ver];
        // vector<vector<int>>adj(ver, vector<int> (0, 0));
        for (int j = 0; j < edg; j++)
        {
            int a, b;
            cin >> a >> b;
            add_edge(adj, a - 1, b - 1);
        }
        printShortestDistance(adj, 0, ver - 1, ver);
        // here i used 0 and ver-1 is because i coded bst and other functions taking 0 to n-1 search
    }

    return 0;
}