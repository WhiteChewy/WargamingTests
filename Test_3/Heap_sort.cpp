#include <vector>
#define SIZE 20

using namespace std;

typedef vector<int> Array;

void _heapify(Array& array, int end, int i) {
	int l = 2 * i + 1;
	int r = 2 * (i + 1);
	int max = i;

	if (l < end && array[i] < array[l])
		max = l;
	if (r < end && array[max] < array[r])
		max = r;
	if (max != i) {
		swap(array[i], array[max]);
		_heapify(array, end, max);
	}
}


Array sortHeap(Array array) {

	int end = (int) array.size();
	int start = end / 2 - 1;

	for (auto i = start; i >= 0; --i) {
		_heapify(array, end, i);
	}

	for (auto i = end - 1; i > 0; --i) {
		std::swap(array[i], array[0]);
		_heapify(array, i, 0);
	}
	return array;
}