#include <stdio.h>
#include <ctype.h>

int main() {
    char str[100];
    int i, j = 0;

    printf("Enter a string: ");
    fgets(str, sizeof(str), stdin);

    for (i = 0; str[i] != '\0'; i++) {
        char ch = tolower(str[i]);
        if (ch!='a' && ch!='e' && ch!='i' && ch!='o' && ch!='u') {
            str[j++] = str[i];   // keep only non-vowels
        }
    }
    str[j] = '\0';  

    printf("String without vowels: %s\n", str);

    return 0;
}
