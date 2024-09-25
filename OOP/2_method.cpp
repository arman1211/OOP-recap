#include <iostream>
#include <string>
using namespace std;

class Genz
{
public:
    // Constructor
    Genz()
    {
        cout << "hello" << endl;
    }

    // Method
    string display()
    {
        cout << "this is genz" << endl;
        return "ok";
    }
};

string display()
{
    cout << "this is another display" << endl;
    return "fine";
}

int main()
{
    Genz a;
    string result = display();
    cout << result << endl;
    return 0;
}
