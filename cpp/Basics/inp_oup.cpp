#include <iostream>
using namespace std;

//  cannot open output file inp_oup.exe: Permission deniedcollect2.exe: error: ld returned 1 exit status
// Error resolution: "Go To task manager and end the task of a.exe or vscode"
int main()
{
    // cout  sample 
    char sample[] = "Hyderabad";
    cout << "I live in " << sample ;
    //cin sample 

    int age;
    cout << "\n Enter your age:";
    cin >> age;
    cout << "\nYour Age is: " << age;

    // cerr sample:cerr is the standard error stream that is used to output the errors.
    cerr << "An Error Occured";

    //clog
    clog << "A Clog Error Occured";
    return 0;
}

