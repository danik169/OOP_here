#include <iostream>
using namespace std;

class Baza {
public:
    Baza() {
        cout << "Constructor Baza" << endl;
    }

    ~Baza() {
        cout << "Destructor Baza" << endl;
    }
};

class Derivata : public Baza {
public:
    Derivata() {
        cout << "Constructor Derivata" << endl;
    }

    ~Derivata() {
        cout << "Destructor Derivata" << endl;
    }
};

int main() {
    Derivata obj;
    return 0;
}
