#include <stdio.h>
#include <string.h>

int buffer[50000001];

#define input 369

int main ()
{
	int pos = 0;
	int value;
	buffer[0] = 0;

	for (value = 1; value <= 2017; value++) {
		pos = (pos + input) % value;
		memmove(buffer+pos+2, buffer+pos+1, value*sizeof(int));
		buffer[pos+1] = value;
		printf ("%d: %d\n", pos, buffer[pos]);
		pos = (pos + 1) % (value + 1);
	}

	printf ("%d: %d, %d: %d\n", pos, buffer[pos], pos+1, buffer[pos+1]);

	for (value = 2018; value <= 50000000; value++) {
		pos = (pos + input) % value;
		memmove(buffer+pos+2, buffer+pos+1, value*sizeof(int));
		buffer[pos+1] = value;
		pos = (pos + 1) % (value + 1);
		if (value % 50000 == 0)
			printf ("%d\n", value);
	}

	printf ("%d: %d, %d: %d\n", 0, buffer[0], 0+1, buffer[0+1]);
}
