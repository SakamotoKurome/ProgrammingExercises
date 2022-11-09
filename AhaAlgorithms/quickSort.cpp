int a[101];

void quicksort(int left, int right)
{
    if (left > right)
    {
        return;
    }
    int temp = a[left];
    int i = left;
    int j = right;
    int t;
    while (i != j)
    {
        while (a[j] >= temp && i < j)
        {
            --j;
        }
        while (a[i] <= temp && i < j)
        {
            ++i;
        }
        if (i < j)
        {
            t = a[i];
            a[i] = a[j];
            a[j] = t;
        }
    }
    a[left] = a[i];
    a[i] = temp;
    quicksort(left, i - 1);
    quicksort(i + 1, right);
}

int main()
{
    return 0;
}