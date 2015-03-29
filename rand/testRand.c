#include <stdlib.h>
#include <stdio.h>

int main(int argc, char *argv[]) {
  int i = 0;
  int IV_0 = 9004;
  int IV_1 = 29395;

  for(i = 100000000; i < 2^32; i++) {
    if((i % 1000000) == 0)
      printf("Testing seed = %d\n", i);
    srand(i);
    if(rand() == IV_0) {
      printf("=========================\n");
      printf("Possible seed = %d\n", i);
      printf("=========================\n");
    }
  }
}
