#include <stdio.h>
#include <stdlib.h>
//By Ted Pinkerton

double* slice(const double list[], const int start, const int end) {
	int i;
	double* new = (double*) malloc((end-start)*sizeof(double));
	if(!new) return NULL;
	for(i = start; i < end; i++) new[i] = list[i];
	return new;
}


int main() {
	double arr[] = {8, 6, 7, 5, 4, 2, 3, 1};
	// double *list = insert(arr, 0, 8);
	double *sliced = slice(arr, 1, 3);
	int i;
	for(i = 1; i <= 3-1; i++) {
		printf("%lf, ", sliced[i]);
	}
	free(sliced);
}