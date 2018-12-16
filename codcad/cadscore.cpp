// http://www.codcad.com/problem/9
#include <iostream>
using namespace std;
int main() {

  int points, levels, score;
  cin >> points >> levels;
  for (int i = 0; i < levels; i++){
    cin >> score;
    points += score;
    if (points < 0){
      points = 0;
    }
    if (points > 100) {
      points = 100;
    }
  }
  cout << points << endl;

}
