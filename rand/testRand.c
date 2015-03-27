#include <stdlib.h>
#include <stdio.h>

int main(int argc, char *argv[]) {
  int seed = atoi(argv[1]);
  srand(seed);
  printf("%d\n", rand());
}
