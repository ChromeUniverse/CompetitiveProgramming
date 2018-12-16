// https://olimpiada.ic.unicamp.br/pratique/pj/2016/f2/fuga/
#include <iostream>
using namespace std;
int main() {

    int h, p ,f ,d;
    cin >> h >> p >> f >> d;

    int position = f;
    while (true) {
        position += d;
        if (position < 0){
          position += 16;
        }
        if (position > 15){
          position -= 16;
        }
        if (position == p) {
            cout << 'N';
            break;
        }
        if (position == h) {
            cout << 'S';
            break;
            }
  }

}
