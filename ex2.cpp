#include <iostream>
using namespace std;

// Clasa de Bază
class Vehicul {
public:
    string marca;

    Vehicul(string m) : marca(m) {
        cout << "Constructor Vehicul: " << marca << endl;
    }

    void porneste() {
        cout << "Vehiculul porneste" << endl;
    }

    ~Vehicul() {
        cout << "Destructor Vehicul" << endl;
    }
};

// Clasa Derivată
class Masina : public Vehicul {
public:
    string model;

    Masina(string m, string mdl) : Vehicul(m), model(mdl) {
        cout << "Constructor Masina: " << model << endl;
    }

    void accelereaza() {
        cout << "Masina accelereaza" << endl;
    }

    ~Masina() {
        cout << "Destructor Masina" << endl;
    }
};

int main() {
    Masina masina("Toyota", "Corolla");
    masina.porneste();
    masina.accelereaza();

    return 0;
}
