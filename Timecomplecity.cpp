// O(log(n))
while (n)
	n /= 2;

// O(sqrt(n))
for (int i = 0; i*i <= n; i++);

// O(n)
for (int i = 0; i < n; i++);

// O(nlog(n))
for (int i = 0; i < n; i++)
	for (int j = i; j; j /= 2);

// O(nsqrt(n))
for (int i = 0; i < n; i++)
	for (int j = 0; j*j <= i; j++);

// O(n^2)
for (int i = 0; i < n; i++)
	for (int j = 0; j < n; j++);

// O(n^3)
for (int i = 0; i < n; i++)
	for (int j = 0; j < n; j++)
		for (int k = 0; k < n; k++);

// O(2^n)
int func(int n) {
	if (n == 0 || n == 1)
		return 1;
	return func(n - 1) + func(n - 2);
}

// O(n!)
// n개의 데이터를 나열하는 방법의 수