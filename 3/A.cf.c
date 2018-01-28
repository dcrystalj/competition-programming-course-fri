int main(int argc, char const *argv[])
{
    double n;
    cin >> n;

    if (n%2 == 0)
        printf(n/2);
    else
        printf(-(n/2+1));


    return 0;
}