// Write a program to find the maximum of three numbers.
// Concepts: if-else if-else statement.

#include <iostream>
using namespace std;

int main(){
    int num1,num2,num3;
    cout << "ENter three number: "; cin >>num1>>num2>>num3;

    if (num1>num2 && num1 > num3){
        cout << "Max number is:  "<<num1<<endl;
    }

    else if (num2 >num1 && num2 > num3){
        cout << "Max number is:  "<<num2<<endl;
    }
    else{
        cout << "Max number is:  "<<num3<<endl;
    }



    return 0;
}