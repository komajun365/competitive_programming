#include<iostream>
#include<vector>
#include<limits>
#include<queue>

using namespace std;

int n,m;
struct place{
    int x,y,c;
};
vector<place> guild;
vector<place> huntp;

struct Edge{
    int c,w;
};
struct Graph{
    vector<vector<Edge>> ve;
};

struct Next{
    int p, now, cost;
};

bool operator < (Next a, Next b) {
    return a.cost > b.cost;
};

struct MinCostMaxFlow{
    Graph g;
    void init(int v){
        g.ve.resize(v);
        for(int i=0;i<v;i++){
            g.ve[i].resize(v);
        };
        for(int i=0;i<v;i++){
            for(int j=0;j<v;j++){
                g.ve[i][j] = {-1,-1};
            }
        }
    }
    void addEdge(int s, int t, int cost, int weight){
        g.ve[s][t]= {cost,weight};
    }

    void show(){
        cout<<"cost"<<endl;
        for(int i=0;i<n+m+2;i++){
            for(int j=0;j<n+m+2;j++)cout<<g.ve[i][j].c<<" ";cout<<endl;
        }
        cout<<"weight"<<endl;
        for(int i=0;i<n+m+2;i++){
            for(int j=0;j<n+m+2;j++)cout<<g.ve[i][j].w<<" ";cout<<endl;
        }
    }
    int run(int s, int t){
        long long ans = 0;
        
        while(1){
            vector<int> prev(n+m+2);
            vector<int> dist(n+m+2);

            for(int i=0;i<n+m+2;i++) prev[i] = -1;
            for(int i=0;i<n+m+2;i++) dist[i] = -1;

            priority_queue<Next> pq;
            pq.push(Next{-1,s,0});
            while(!pq.empty()){
                Next now = pq.top();
                pq.pop();
                if(dist[now.now] != -1 && dist[now.now] <= now.cost){
                    continue;
                }
                dist[now.now] = now.cost;
                prev[now.now] = now.p;
                for(int i=0;i<n+m+2;i++){
                    if(g.ve[now.now][i].w <= 0)continue;
                    if(dist[i] != -1 && dist[i] < dist[now.now] + g.ve[now.now][i].c) continue;
                    pq.push(Next{now.now, i, dist[now.now] + g.ve[now.now][i].c});
                }
            }

            //for(int i=0;i<n+m+2;i++) cout<<prev[i]<<" ";cout<<endl;
            //for(int i=0;i<n+m+2;i++) cout<<dist[i]<<" ";cout<<endl;


            if(dist[t] != -1){
                int mi = std::numeric_limits<int>::max();
                int p = t;
                while(prev[p]!= -1){
                    mi = min(mi, g.ve[prev[p]][p].w);
                    p = prev[p];
                }
                p = t;
                int tmpcost = 0;
                while(prev[p]!=-1){
                    g.ve[prev[p]][p].w -= mi;
                    g.ve[p][prev[p]].w += mi;
                    tmpcost += g.ve[prev[p]][p].c;
                    p = prev[p];
                }
                //cout<<mi<<" "<<tmpcost<<endl; 
                ans += (long long)mi*(long long)tmpcost;
                //show();
            } else {
                break;
            }
            //cout<<ans<<endl;
        }

        return ans;
    }
};

int main(){
    cin>>m>>n;
    for(int i=0;i<m;i++){
        int xp,yp,cp;
        cin>>xp>>yp>>cp;
        huntp.emplace_back(place{xp,yp,cp});
    }
    /*for(auto a: huntp){
        cout<<"huntp "<<a.x<<" "<<a.y<<" "<<a.c<<endl;
    }*/
    for(int i=0;i<n;i++){
        int xp,yp,cp;
        cin>>xp>>yp>>cp;
        guild.emplace_back(place{xp,yp,cp});        
    }
    /*for(auto a: guild){
        cout<<"guild "<<a.x<<" "<<a.y<<" "<<a.c<<endl;
    }*/

    MinCostMaxFlow mcf;
    mcf.init(m+n+2);
    for(int i=0;i<m;i++){
        mcf.addEdge(0,2+i,0,huntp[i].c);
        mcf.addEdge(2+i,0,0,0);
    }
    int ma = std::numeric_limits<int>::max();
    for(int i=0;i<m;i++){
        for(int j=0;j<n;j++){
            int dist = abs(huntp[i].x-guild[j].x)+abs(huntp[i].y-guild[j].y)+1;
            mcf.addEdge(2+i,2+m+j,dist,ma);
            mcf.addEdge(2+m+j,2+i,-dist,0);
        }
    }
    for(int i=0;i<n;i++){
        mcf.addEdge(2+m+i,1,0,guild[i].c);
        mcf.addEdge(1,2+m+i,0,0);
    }
    //mcf.show();
    int ans = mcf.run(0,1);
    cout<<ans<<endl;

    return 0;
}