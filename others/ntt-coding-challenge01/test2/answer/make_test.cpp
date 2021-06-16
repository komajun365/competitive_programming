#include<random>
#include<iostream>

using namespace std;

int main(){
	std::random_device rnd;
    while(1){
        int a = rnd()%100+1;
        int b = rnd()%100+1;
        if((a*b)%(a+b) == 0){
            cout<<a<<" "<<b<<endl;
            break;
        }
    }
    return 0;
}

