#include <iostream>
using namespace std;

class ClasaB;

class ClasaA {
private:
    int valoareA;

public:
    ClasaA(int a) : valoareA(a) {}

    // Declararea clasei ClasaB ca prietenă
    friend class ClasaB;
};

class ClasaB {
private:
    int valoareB;

public:
    ClasaB(int b) : valoareB(b) {}

    // Acces la membrul privat al clasei ClasaA
    void afiseazaValori(ClasaA& a) {
        cout << "Valoare ClasaA: " << a.valoareA << ", Valoare ClasaB: " << valoareB << endl;
    }
};

int main() {
    ClasaA a(10);
    ClasaB b(20);

    b.afiseazaValori(a);
    return 0;
}
