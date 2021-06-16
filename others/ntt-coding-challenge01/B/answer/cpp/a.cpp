#include<iostream>
#include<string>
#include<vector>

using namespace std;

int n,m;
int table[100][100];

void U(){
    for(int i=0;i<m;i++){
        vector<int> nextvec;
        int prev = -1;
        for(int j=0;j<n;j++){
            if(table[j][i] == 0) continue;
            if(prev == -1) prev = table[j][i];
            else {
                if(prev == table[j][i]){
                    nextvec.push_back(prev*2);
                    prev = -1;
                } else {
                    nextvec.push_back(prev);
                    prev = table[j][i];
                }
            }
        }
        if(prev != -1){
            nextvec.push_back(prev);
        }
        for(int j=0;j<n;j++){
            if(j < nextvec.size()) table[j][i] = nextvec[j];
            else table[j][i] = 0;
        }
    }
    return;
}

void D(){
    for(int i=0;i<m;i++){
        vector<int> nextvec;
        int prev = -1;
        for(int j=n-1;j>=0;j--){
            if(table[j][i] == 0) continue;
            if(prev == -1) prev = table[j][i];
            else {
                if(prev == table[j][i]){
                    nextvec.push_back(prev*2);
                    prev = -1;
                } else {
                    nextvec.push_back(prev);
                    prev = table[j][i];
                }
            }
        }
        if(prev != -1){
            nextvec.push_back(prev);
        }
        for(int j=0;j<n;j++){
            if(j < nextvec.size()) table[n-j-1][i] = nextvec[j];
            else table[n-j-1][i] = 0;
        }
    }
    return;
}

void L(){
    for(int i=0;i<n;i++){
        vector<int> nextvec;
        int prev = -1;
        for(int j=0;j<m;j++){
            if(table[i][j] == 0) continue;
            if(prev == -1) prev = table[i][j];
            else {
                if(prev == table[i][j]){
                    nextvec.push_back(prev*2);
                    prev = -1;
                } else {
                    nextvec.push_back(prev);
                    prev = table[i][j];
                }
            }
        }
        if(prev != -1){
            nextvec.push_back(prev);
        }
        for(int j=0;j<m;j++){
            if(j < nextvec.size()) table[i][j] = nextvec[j];
            else table[i][j] = 0;
        }
    }
    return;
}

void R(){
    for(int i=0;i<n;i++){
        vector<int> nextvec;
        int prev = -1;
        for(int j=m-1;j>=0;j--){
            if(table[i][j] == 0) continue;
            if(prev == -1) prev = table[i][j];
            else {
                if(prev == table[i][j]){
                    nextvec.push_back(prev*2);
                    prev = -1;
                } else {
                    nextvec.push_back(prev);
                    prev = table[i][j];
                }
            }
        }
        if(prev != -1){
            nextvec.push_back(prev);
        }
        for(int j=0;j<m;j++){
            if(j < nextvec.size()) table[i][m-j-1] = nextvec[j];
            else table[i][m-j-1] = 0;
        }
    }
    return;
}

void rotate(char i){
    if(i == 'R') R();
    if(i == 'L') L();
    if(i == 'D') D();
    if(i == 'U') U();
    return;
}


int main(){
    cin>>n>>m;
    for(int i=0;i<n;i++){
        for(int j=0;j<m;j++){
            cin>>table[i][j];
        }
    }
    string s;
    cin>>s;
    for(int i=0;i<s.size();i++){
        rotate(s[i]);
    }
    for(int i=0;i<n;i++){
        for(int j=0;j<m-1;j++){
            cout<<table[i][j]<<" ";
        }cout<<table[i][m-1]<<endl;
    }
    return 0;
}