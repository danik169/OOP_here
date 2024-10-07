#include <iostream>
using namespace std;

class Prieten {
private:
    int secret;

public:
    Prieten(int s) : secret(s) {}

    // Declararea unei funcții friend
    friend void afiseazaSecretul(Prieten p);
};

// Funcția friend care accesează atributele private
void afiseazaSecretul(Prieten p) {
    cout << "Secretul este: " << p.secret << endl;
}

int main() {
    Prieten p(42);
    afiseazaSecretul(p);
    return 0;
}
