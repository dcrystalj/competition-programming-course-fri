#include <stdio.h>
using namespace std;

int main()
{

    long long n;
    scanf("%I64d", &n);
    long long m = n/2;
    if (n%2 == 0)
        printf("%I64d", m);
    else
        printf("%I64d",-m-1);


    return 0;
}