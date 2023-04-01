#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

int main(int argc, char **argv) 
{ 
 char buff[5]; 
 printf("Exploiting via returnig into libc function\n"); 
 strcpy(buff, argv[1]);
 printf("You typed: %s\n", buff); 
 return(0); 
}
