

#include <iostream>
using namespace std;

int main(){
    int y;
    cin >> y;

    while (true){
        y +=1;
        
        int a = y / 1000;
        int b = y / 100 % 10;
        int c = y / 10 % 10;
        int d = y % 10;

        if (a != b && a != c && a !=d && b !=c && b != d && c !=d){
            break;
        }

        cout << y<< endl;

        return 0;
    }
}


/*

python solution

year = int(input())



cout = year

while cout <= 9000:
    year +=1
    cout += 1

    ans = str(year)

    a = str(ans[0])
    b = str(ans[1])
    c = str(ans[2])
    d =  str(ans[3])

    if (a !=b) and (a !=c) and (a != d) and (b != c) and (b != d) and (c != d):
        print(year)
        break
    


*/