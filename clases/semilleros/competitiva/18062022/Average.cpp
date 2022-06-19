#include <bits/stdc++.h>
using namespace std;
#define forn(i,n) for(int i = 0; i<n; i++)
#define for1(i,n) for(int i = 1; i<n; i++)
#define fore(i, l, r) for (int i = (int)l; i <= (int)r; i++)
#define forr(i, n) for (int i = (int)(n)-1; i >= 0; i--)
#define line cout<<'--------------'<<nl
#define nl endl
#define pb push_back
#define fi first
#define sec second
#define sz(v) ((int)v.size())
#define all(v) v.begin(), v.end()
#define allr(v) v.rbegin(), v.rend()
#define isOdd(x) ((int)x & 1)

typedef long long ll;
typedef vector<int> vi;
const int inf = 2147483647;


int main(){
    // freopen('i.txt', 'r', stdin);
    // freopen('o.txt', 'w', stdout);
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    cout << setprecision(20) << fixed;

    string s;cin>>s;

    int suma = 0;
    int promedio;
    forn(i,s.size()){
        suma+=s[i];
    }

    promedio = suma/s.size();
    if(s==" "){
        cout<<" ";
    }else{
        cout<<(char)(promedio)<<nl;
    }
    return 0;
}