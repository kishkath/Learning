#include <iostream>
using namespace std;
#include <bits/stdc++.h>
int main()
{
    for (int i=1;i<=5;i++){
        cout << "Hey!\n";
        
    }
    int arr[] {40,50,10,20,30,40,55};
    for (auto el:arr){
        cout << el <<" ";
    }

    //using stl vector

    vector<int> v={1,2,3,4};
    for (vector<int>::iterator it = v.begin();it!=v.end();it++){
        cout << *it << "\t";
    }
    return 0;
}