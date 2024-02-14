// Write a program to check if a given number is positive, negative, or zero.
// Concepts: if-else if-else statement.

#include <iostream>

using namespace std;

int main()
{
    int num; 
    cout << "Enter a number:  "<<endl; cin >>num;


    if (num > 0){
        cout << num << " is postive number"<<endl;
    }
    else if (num ==0){
        cout << "the number is zero"<<endl;
    }

    else{
        cout << num << " is negative"
    }


    return 0;
}