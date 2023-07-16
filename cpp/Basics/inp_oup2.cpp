#include <iostream>
#include <ios>
#include <limits>
using namespace std;

int main()
{
    int a;
    string s;

    cin >> a;

    //discards input buffer
    //cin.ignore(numeric_limits<streamsize>::max(),'\n');
    
    //discards input buffer and initial white spaces
    cin >> ws;

    getline(cin,s);

    cout << a << endl;
    cout << s << endl;
    return 0;
}