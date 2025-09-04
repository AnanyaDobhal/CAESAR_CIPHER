#include <iostream>
#include <string>
using namespace std;

string caesarCipher(string text, int shift, bool encrypt) {
    string result = "";
    if (!encrypt) shift = -shift;

    for (char c : text) {
        if (isalpha(c)) {
            char base = isupper(c) ? 'A' : 'a';
            result += char((c - base + shift + 26) % 26 + base);
        } else {
            result += c;
        }
    }
    return result;
}

int main() {
    string mode;
    getline(cin, mode);

    string text;
    getline(cin, text);

    int shift;
    cin >> shift;

    bool encrypt = (mode == "encrypt");
    string output = caesarCipher(text, shift, encrypt);
    cout << output << endl;

    return 0;
}
