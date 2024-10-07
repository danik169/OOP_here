#include <iostream>
using namespace std;

class Student {
private:
    string nume;
    int varsta;

public:
    // Constructor
    Student(string n, int v) {
        nume = std::move(n);
        varsta = v;
    }

    // Getter pentru nume
    string getNume() {
        return nume;
    }

    // Setter pentru nume
    void setNume(string n) {
        nume = n;
    }

    // Getter pentru varsta
    int getVarsta() const{
        return varsta;
    }

    // Setter pentru varsta
    void setVarsta(int v) {
        varsta = v;
    }

    // Metodă pentru afișarea detaliilor
    void afiseazaDetalii() {
        cout << "Nume: " << nume << ", Varsta: " << varsta << endl;
    }
};

int main() {
    // Creare obiect Student
    Student s("Ion Popescu", 20);

    // Accesare prin metodele getter și setter
    s.afiseazaDetalii();
    s.setNume("Maria Ionescu");
    s.setVarsta(22);

    s.afiseazaDetalii();
    return 0;
}
