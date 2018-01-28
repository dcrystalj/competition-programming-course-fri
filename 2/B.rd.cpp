#include <iostream>
#include <string.h>
#include <algorithm>
#include <stdio.h>
using namespace std;


int main()
{
    char a [10000];
    char b [10000];
    char d;
    char* max;
    cin >> a;
    cin >> b;

    int len_a = strlen(a);
    int len_b = strlen(b);
    char* blen = b+len_b;
    int changed = 1;
    int num_of_changes = 0;
    for (int i = 0; i < len_a; ++i)
    {
        if (changed)
            max = max_element(b, blen);
        if (max[0] > a[i])
        {
            a[i] = max[0];
            max[0] = '0';
            changed = 1;
            num_of_changes++;
        }
        else changed = 0;

        if (num_of_changes == len_b) break;
    }

    cout << a;

    return 0;
}