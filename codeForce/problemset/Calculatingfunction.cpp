// https://codeforces.com/problemset/problem/486/A

#include <iostream>

using namespace std;

int main(){
    long long num;
    cin >> num;

    if (num % 2 == 0){
        cout << num / 2 <<endl;
    }else{
        cout << -(num + 1)/2 <<endl;
    }

    return 0;
}