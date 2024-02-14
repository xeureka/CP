// Write a program to check if a given year is a leap year or not.
// Concepts: if-else if-else statement.

#include <iostream>
using namespace std;

int main()
{

    int year;
    cout << "Enter the year:  ";cin >>year;

    if (year % 4 ==0){
        if (year % 100 ==0){
            if (year % 400 ==0){
                cout <<"Leap year";
            }
            else{
                cout << "Not leap year";
            }
        else{
            cout << "Leap Year";
            }
    else{
        cout << "Not leap year";
    }
        }
    }




    return 0;
}