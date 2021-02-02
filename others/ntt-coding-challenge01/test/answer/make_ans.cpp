#include <random>
#include<iostream>

using namespace std;

int main(){
	std::random_device rnd;
	int a = rnd()%100;
    int b = rnd()%100;
    cout<<a<<" "<<b<<endl; 
	return 0;
}

