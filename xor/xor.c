#include <stdio.h>
#include <string.h>

/* Source code:
int main() {
  char flag[] = "ADCTF_XXXXXXXXXXXXXXXXXXXX";
  int len = strlen(flag);
  for (int i = 0; i < len; i++) {
    if (i > 0) flag[i] ^= flag[i-1];
    flag[i] ^= flag[i] >> 4;
    flag[i] ^= flag[i] >> 3;
    flag[i] ^= flag[i] >> 2;
    flag[i] ^= flag[i] >> 1;
    printf("%02x", (unsigned char)flag[i]);
  }
  return 0;
}
*/

int main() {
  char flag[] = {0x71, 0x22, 0x49, 0x14, 0x6f, 0x24, 0x1d, 0x31, 0x65, 0x1a, 0x50, 0x4a, 0x1a, 0x73, 0x72, 0x38, 0x4d, 0x17, 0x3f, 0x7f, 0x79, 0x0c, 0x2b, 0x11, 0x5f, 0x47};
  char encrypted_flag[] = {0x71, 0x22, 0x49, 0x14, 0x6f, 0x24, 0x1d, 0x31, 0x65, 0x1a, 0x50, 0x4a, 0x1a, 0x73, 0x72, 0x38, 0x4d, 0x17, 0x3f, 0x7f, 0x79, 0x0c, 0x2b, 0x11, 0x5f, 0x47};
  int len = strlen(flag);
  int i = 0;
  for (; i < len; i++) {
      // Each char is 8 bits
      // We need to xor and shift by 1 a total of 8 times
      // We need to xor and shift by 2 a total of 4 times
      // We need to xor and shift by 3 a total of 4 times
      // We need to xor and shift by 4 a total of 2 times
      flag[i] ^= flag[i] >> 1;
      flag[i] ^= flag[i] >> 1;
      flag[i] ^= flag[i] >> 1;
      flag[i] ^= flag[i] >> 1;
      flag[i] ^= flag[i] >> 1;
      flag[i] ^= flag[i] >> 1;
      flag[i] ^= flag[i] >> 1;
      flag[i] ^= flag[i] >> 2;
      flag[i] ^= flag[i] >> 2;
      flag[i] ^= flag[i] >> 2;
      flag[i] ^= flag[i] >> 3;
      flag[i] ^= flag[i] >> 3;
      flag[i] ^= flag[i] >> 3;
      flag[i] ^= flag[i] >> 4;
      if (i > 0) flag[i] ^= encrypted_flag[i-1];
      // Prints out the hexadecimal ascii-encoded flag
      printf("%02x", (unsigned char)flag[i]);
  }
}
