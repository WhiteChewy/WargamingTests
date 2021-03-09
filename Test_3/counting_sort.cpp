void countingSort(int* array, int n, int k) {
 	int c[k+1] = { 0 };
 	for (int i = 0; i < n; ++i) {
 		++c[array[i]];
 	}

 	int b = 0;
 	for (int i = 0; i < k+1; ++i){
 		for (int j = 0; j < c[i]; ++j) {
 			array[b++] = i;
 		}
 	}
 }