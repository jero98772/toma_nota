#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <unordered_map>
#include <string.h>
#include <math.h>
#include <queue>
#include <set>
 
#define DBG(x) cerr << #x << " = " << (x) << endl
#define RAYA cerr << "=============================" << endl
 
#define fi first
#define se second
#define forn(i, n) for (int i = 0; i < (int)n; ++i)
#define for1(i, n) for (int i = 1; i <= (int)n; ++i)
#define fore(i, l, r) for (int i = (int)l; i <= (int)r; ++i)
#define ford(i, n) for (int i = (int)(n)-1; i >= 0; --i)
#define fored(i, l, r) for (int i = (int)r; i >= (int)l; --i)
#define pb push_back
#define el '\n'
#define d(x) cout << #x << " " << x << el
#define ri(n) scanf("%d", &n)
#define sz(v) ((int)v.size())
#define all(v) v.begin(), v.end()
#define allr(v) v.rbegin(), v.rend()
 
using namespace std;
 
typedef long long ll;
typedef double ld;
typedef pair<ll, ll> ii;
typedef pair<pair<ll, ll>, ll> iii;
 
typedef pair<char, int> pci;
typedef pair<ll, ll> pll;
typedef vector<int> vi;
typedef vector<char> vc;
 
const int inf = 1e9;
const int MAXS = 1e5 + 2;
const int MAXT = 1e2 + 2;
 
int dx[] = {1, -1, 0, 0, 1, -1, -1, 1};
int dy[] = {0, 0, 1, -1, 1, 1, -1, -1};
const int MAX = 9999991 + 1;
void solve()
{
    // code
    int n;
    cin >> n;
    vi sieve(MAX, 0);//inicialisar el vector?
    for (int i = 4; i < MAX; i += 2)
        sieve[i] = 1;
    fore(i, 3, MAX - 1)
    {
        if (!sieve[i])
        {
            for (int j = i + i; j < MAX; j += i)
            {
                sieve[j] = 1;
            }
        }
    }
    vi primos;
    fore(i, 2, MAX - 1)
    {
        if (!sieve[i])
            primos.pb(i);
    }
 
    forn(i, n)
    {
        ll a, b;
        cin >> a >> b;
        b *= a;
        unordered_map<int, int> um;
        for (int j = 0; j < primos.size(); j++)
        {
            if (!b)
                break;
            if (b % primos[j] == 0)
                while (b > 0)
                {
                    if (b % primos[j] != 0)
                        break;
 
                    b /= primos[j];
                    um[primos[j]] = 1;
                }
        }
        cout << um.size() << "\n";
    }
}
int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    int tt;
    tt = 1;
    // cin >> tt;
    while (tt--)
        solve();
    return 0;
}
