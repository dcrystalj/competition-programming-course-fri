int n,x[100];
int f[100]; //memoizacija
int solve (int i) {
    if (i >= n) return 0;
    if (f[i] != -1) return f[i];
    int r1 = x[i] + solve(i+2);
    int r2 = x[i] + solve(i+1);
    return max(r1, r2);

}
int main(int argc, char const *argv[])
{
    for (int i = 0; i < count; ++i)
    {
        cin >> x[i];
        f[i] = -1;
    }
    //beres iz fajla v stdin
    fropen("dp.in", "r", stdin);

    //prepises z -1 cel array
    memset(f, -1, sizeof(f))
    int r = solve(0);
    cout << r << endl;
    return 0;
}


////////////// LONGEST INCREASING SUBSEQUENCE

for (int i = 0; i < n; ++i)
{
    f[i] = 1;
    for (int j = 0; j <= i-1; ++j)
    {
        if (x[j] < x[i])
        f[j] = max(f[i], f[j]+1);
    }
}