#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

// Shellcode

void main(int argc, char *argv[]) {
 char buffer[250];
 strcpy(buffer, argv[1]);
 printf("buffer addres is at: %p \n", buffer);
 printf("You entered: %s \n", buffer);
 return;
}
