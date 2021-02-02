#include <random>
#include<iostream>

using namespace std;

int vec[6] = {2,4,8,16,32,64};
char st[4] = {'U','L','R','D'};

int main(){
	std::random_device rnd;
	int a = 50 +rnd()%50;
    int b = 50 +rnd()%50;
    cout<<a<<" "<<b<<endl;
    for(int i=0;i<a;i++){
        for(int j=0;j<b-1;j++){
            int k = rnd()%6;
            cout<<vec[k]<<" ";
        }
        int k = rnd()%6;
        cout<<vec[k]<<endl;
    }
    a = rnd()%100;
    for(int i=0;i<a;i++){
        int k = rnd()%4;
        cout<<st[k];
    }
    cout<<endl;

	return 0;
}

