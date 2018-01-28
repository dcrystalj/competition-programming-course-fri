#include <math.h>
#include <stdio.h>

using namespace std;

int main()
{

    int n;
    int k;
    int summer;
    int tmp;
    scanf("%d %d", &n, &k);

    float q = 1.0/k;
    float q30 = pow(q, 30);
    float f = (1-q30) / (1-q);

    if (k > n)
    {
        printf("%d", n);
    }
    else
    {
        for (int i = n - n/k; i < 10000000000; ++i)
        {
            int a = i * f;
            if (a >= n)
            {
                summer = i;
                tmp = i;

                while (tmp >= k)
                {
                    tmp = tmp/k;
                    summer += tmp;
                }

                if (summer >= n)
                {
                    printf("%d", i);
                    break;
                }
            }
        }
   }

   return 0;
}