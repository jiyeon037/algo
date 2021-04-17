#include<stdio.h>
#define min(a,b) (a) < (b) ? (a) : (b)
int main() {
	int x, y, w, h;
	scanf_s("%d %d %d %d", &x, &y, &w, &h);
	printf("%d", min(x, min(y, min(w - x, h - y))));
}