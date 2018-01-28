#include <stdio.h>
#include <float.h>
#include <math.h>
#include <algorithm>

using namespace std;

int main()
{
    int n;
    scanf("%d", &n);

    int v [n];
    int s [n];

    double l = 0;
    double h = 10000000000;
    double m = 1;

    bool isNegative = false;
    bool isPositive = false;

    for (int i = 0; i < n; ++i)
    {
        scanf("%d %d", &s[i], &v[i]);
        if (v[i] > 0)
            isPositive = true;
        if (v[i] < 0 && isPositive)
            isNegative = true;
    }

    if ( !isNegative )
    {
        printf("-1.0000000000");
        return 0;
    }

    double left, right;
    bool a, b;
    while (fabs(h-l) > 0.0000000001)
    {
        m = (h+l) / 2.0;
        a = false;
        b = false;

        for (int i = 0; i < n; ++i)
        {
            if (v[i] > 0)
            {
                if (!b)
                {
                    right = s[i] + v[i] * m;
                    b = true;
                }
                else
                    right = max(right, s[i] + v[i] * m);
            }
            else if (b)
            {
                left = s[i] + v[i] * m;
                if (right - left > 0)
                {
                    h = m;
                    a = true;
                    break;
                }
            }
        }

        if (!a)
            l = m;
    }

    printf("%.10f", h);
    return 0;
}