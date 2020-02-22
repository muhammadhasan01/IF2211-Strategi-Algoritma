#include <bits/stdc++.h>

using namespace std;

const double INF = 1e9;
const double eps = 1e-12;

struct point {
  double x, y;

  bool operator == (const point &pt) {
    return (x == pt.x && y == pt.y);
  }
};

struct line {
  double gradien, constant;

  line(point a, point b) {
    gradien = (a.x == b.x ? INF : (b.y - a.y) / (b.x - a.x));
    constant = a.y - gradien * a.x;
  }

  double inputX(double x) {
    return gradien * x + constant;
  }
};

int jumlahTitik;
double hasilWaktu;
point ujungTitik;
clock_t timer;
vector<point> titik;
vector<point> convexHull;
vector<bool> mark;

int main() {
  srand(time(NULL));
  cout << "Masukkan jumlah titik yang diinginkan : ";
  cin >> jumlahTitik;
  titik.resize(jumlahTitik);
  mark.resize(jumlahTitik);
  for (int i = 0; i < jumlahTitik; i++) {
    bool isTitikValid;
    do {
      isTitikValid = true;
      titik[i].x = rand() % 101;
      titik[i].y = rand() % 101;
      for (int j = i - 1; j >= 0; j--) {
        if (titik[j] == titik[i]) {
          isTitikValid = false;
          break;
        }
      }
    } while (!isTitikValid);
    mark[i] = 0;
  }
  timer = clock();
  int idxTitikTeratas = 0;
  for (int i = 1; i < jumlahTitik; i++) {
    if (titik[i].y > titik[idxTitikTeratas].y) {
      idxTitikTeratas = i;
    }
  }
  convexHull.push_back(titik[idxTitikTeratas]);
  mark[idxTitikTeratas] = 1;
  for (int i = 0; i < jumlahTitik; i++) {
    bool masihAda = false;
    ujungTitik = convexHull[i];
    bool dbg = false;
    for (int j = 0; j < jumlahTitik; j++) {
      if (mark[j]) continue;
      line garisHubung(ujungTitik, titik[j]);
      if (i == 2 && j == jumlahTitik - 1) dbg = true;
      int jumlahDiatas = 0, jumlahDibawah = 0;
      bool isTitikValid = true;
      for (int k = 0; k < jumlahTitik; k++) {
        if (k == j) continue;
        double ord = titik[k].y;
        double hasilInput = garisHubung.inputX(titik[k].x);
        if (ord - hasilInput > eps) jumlahDiatas++;
        else if (eps < hasilInput - ord) jumlahDibawah++;
        if (jumlahDiatas > 0 && jumlahDibawah > 0) {
          isTitikValid = false;
          break;
        }
      }
      if (isTitikValid) {
        convexHull.push_back(titik[j]);
        mark[j] = 1;
        masihAda = true;
        break;
      }
    }
    if (!masihAda) break;
  }
  convexHull.push_back(convexHull[0]);
  hasilWaktu = (1000.0) * (clock() - timer) / CLOCKS_PER_SEC;
  cout << "Titik-titik yang di generate adalah : \n";
  for (point pt : titik) {
    cout << "(" << pt.x << "," << pt.y << ")" << '\n';
  }
  cout << '\n';
  cout << "Hasil senarai (list) titik-titik convexhull adalah : \n";
  for (point titikConvex : convexHull) {
    cout << "(" << titikConvex.x << "," << titikConvex.y << ")" << '\n';
  }
  cout << '\n';
  cout << "Hasil waktu eksekusi (tanpa memperhitungkan I/O) : ";
  cout << fixed << setprecision(5) << hasilWaktu << " ms\n";
  return 0;
}
