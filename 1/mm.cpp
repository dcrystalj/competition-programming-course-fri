#include <iostream>
#include <algorithm>
#include <stdio.h>

using namespace std;

int main(int argc, char const *argv[])
{
    signed long long n,k;
    cin >> n >> k;
    signed long long v[n];

    for (signed long long i = 0; i < n; ++i)
    {
        cin >> v[i];
    }

    k--;

    std::sort(v,v+n);
    printf ("%I64d %I64d", v[k/n], v[k%n]);
    //cout << v[k/n] << " " << v[k%n];
    return 0;
}



