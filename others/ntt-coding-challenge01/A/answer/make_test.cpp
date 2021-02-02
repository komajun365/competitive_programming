#include <random>
#include<iostream>

using namespace std;

int main(){
	std::random_device rnd;
	int a = rnd()%180;
	if(a == 0) a+=2;
	if(a % 2) a--;
	if(a == 0) a+=2;
	cout<<a<<endl;
	return 0;
}

