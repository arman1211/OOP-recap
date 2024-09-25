#include <iostream>
#include <string>
using namespace std;

class Car
{
public:
    string make;
    string model;
    int year;

    Car(string carMake, string carModel, int carYear)
    {
        make = carMake;
        model = carModel;
        year = carYear;
    }

    void startEngine()
    {
        cout << "pipippppppppppp" << endl;
    }
};

int main()
{

    Car myCar("porche", "dfs", 2022);

    cout << myCar.make << endl;
    cout << myCar.model << endl;
    cout << myCar.year << endl;

    myCar.year = 2023;
    cout << myCar.year << endl;

    myCar.startEngine();

    return 0;
}
