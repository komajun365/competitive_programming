#include<iostream>
#include<vector>
#include<unordered_set>
#include<algorithm>

using namespace std;

int n,m;
vector<long long> l;
unordered_set<long long> st;
long long ll[1000*1000+2];

int main(){

    cin>>n>>m;
    for(int i=0;i<n;i++){
        long long inp;cin>>inp;
        l.push_back(inp*inp);
    }

    for(int i=0;i<n;i++){
        st.insert(l[i]);
    }

    sort(l.begin(),l.end());

    long long ans = 0;
    for(int i=0;i<n;i++){
        for(int j=i+1;j<n;j++){
            if(st.find(l[i]+l[j]) != st.end()) ans += 1;
        }
    }

    int top = 0;
    int now = 1;
    l.push_back(-1);
    for(int i=1;i<l.size();i++){
        if(l[i-1] != l[i]){
            top = max(top,now);
            now = 1;
        } else {
            now++;
        }
    }

    int anstmp = 0;
    if(m>=2){
        anstmp = m*(m-1)*top/2;
    }

    int cnt = 0;
    for(int i=0;i<n;i++){
        for(int j=i+1;j<n;j++){
            ll[cnt] = l[i] + l[j];
            cnt++;
            if(l[j]-l[i] > 0) {
                ll[cnt] = l[j]-l[i];
                cnt++;
            }
        }
    }
    sort(ll,ll+cnt);
    ll[cnt] = -1;
    cnt++;
    top = 0;
    now = 1;
    for(int i=1;i<cnt;i++){
        if(ll[i-1] != ll[i]){
            top = max(top,now);
            now = 1;
        } else {
            now++;
        }
    }
    anstmp = max(anstmp, top*m);
    ans += anstmp;

    cout<<ans<<endl;
}