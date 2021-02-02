#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

//Q1
char *my_strcat(char *dest, const char *src) {
    int i, j;
    for (i = 0; dest[i] != '\0'; i++);
    for (j = 0; src[j] != '\0'; j++) {
        dest[i + j] = src[j];
    }
    dest[i + j] = '\0';
    return dest;
}

//Q2
int my_strcmp_rec(char str1[], char str2[]) {
    if(*str1 && (*str1 == *str2)) {
        return my_strcmp_rec(str1+1, str2+1);
    }
    return *(const unsigned char*)str1-*(const unsigned char*)str2;
}

//Q3
int my_atoi(char *str) {
    int total = 0;
    for(int i = 0; str[i] != '\0'; i++) {
        if(isdigit(str[i])) {
            total = total*10 + (int) str[i]-'0';
        }
    }
    return total;
}

//Q4
int cycles(struct node* head) {
    struct node* hare, tort = head, head;
    while(hare != NULL) {
        hare = hare->next;
        if(hare != NULL) hare = hare->next;
        tort = tort->next;
        if(hare == tort) return 1;
    }
    return 0;
}

int main() {
    char str1[80] = "Hello, ";
    char str2[] = "World!";
    printf("%s\n", my_strcat(str1, str2));

    char str3[] = "World!";
    printf("%d\n", my_strcmp_rec(str2, str3));

    printf("%d\n", my_atoi("1234567890"));
    return 0;
}