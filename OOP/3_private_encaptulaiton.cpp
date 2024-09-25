#include <iostream>
#include <string>
using namespace std;

class Status
{
private:
    string status; // Private variable
    // Private method
    void married()
    {
        cout << "This is a private method" << endl;
    }

public:
    string name; // Public variable

    // Constructor
    Status()
    {
        status = "Single";
        name = "Arman";
    }

    string getStatus()
    {
        return status;
    }

    void getMarried()
    {
        married(); // Call private method
    }
    string setStatus(string newStatus)
    {
        status = newStatus;
        return "done";
    }
};

class New : public Status
{
public:
    // Constructor
    New() : Status() {}

    string getStatus()
    {
        return Status::getStatus();
    }
};

int main()
{

    Status myobj;
    New newObj;

    cout << newObj.setStatus("mm") << endl;
    cout << myobj.getStatus() << endl;

    myobj.getMarried();
    cout << "Name: " << myobj.name << ", Status: " << myobj.getStatus() << endl;

    myobj.setStatus("Engaged");
    cout << myobj.getStatus() << endl;

    return 0;
}
