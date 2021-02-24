#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

#include "autocomplete.h"

#define MAXLINE 200

int termcmp(struct term term1, struct term term2) {
    return strcmp(term1.term, term2.term);
}

void read_in_terms(struct term **terms, int *pnterms, char *filename) {
    FILE *fp = fopen(filename, "r");
    if (fp == NULL) {
        perror("Error while opening the file.\n");
        exit(EXIT_FAILURE);
    }

    int lines;
    int weight;
    char text[MAXLINE];
    fscanf(fp, "%d\n", &lines);
    *pnterms = lines;
    *terms = (struct term *) calloc(lines, sizeof(struct term));

    for(int i = 0; i < lines; i++) {
        fscanf(fp, "%d %[^\n]s", &weight, text);
        (*terms)[i].weight = weight;
        strcpy((*terms)[i].term, text);
    }

    fclose(fp);
    qsort(*terms, lines, sizeof(struct term), termcmp);
}

int mstrcmp(char str1[], char str2[]) {
    if (*str1 == '\0') {
        return 0;
    }
    if(*str1 && (*str1 == *str2)) {
        return mstrcmp(str1+1, str2+1);
    }
    return *(const unsigned char*)str1-*(const unsigned char*)str2;
}

int match(struct term *terms, int nterms, char *substr) {
    int first = 0;
    int last = nterms-1;
    int middle = last/2;
    while(first <= last) {
        printf("%d, %d, %d\n", first, middle, last);
        printf("%s\n", terms[middle].term);
        int cmp = mstrcmp(terms[middle].term, substr);
        printf("%d\n", cmp);
        if(cmp < 0) {
            first = middle+1;
        }
        else if(cmp > 0) {
            last = middle-1;
        }
        else {
            return middle;
        }
        middle = (first+last)/2;
    }
}

int lowest_match(struct term *terms, int nterms, char *substr) {
    int i;
    for(i = match(terms, nterms, substr); mstrcmp(terms[i].term, substr) != 0; i--);
    return i+1;
}

int highest_match(struct term *terms, int nterms, char *substr) {
    int i;
    for(i = match(terms, nterms, substr); mstrcmp(terms[i].term, substr) != 0; i++);
    return i-1;
}

void autocomplete(struct term **answer, int *n_answer, struct term *terms, int nterms, char *substr) {

}


int main(void) {
    struct term* terms;
    int nterms;
    read_in_terms(&terms, &nterms, "cities.txt");
    printf("%d\n", nterms);
    printf("%s\n", terms[1].term);
    lowest_match(terms, nterms, "Tor");
    // highest_match(terms, nterms, "Tor");
    
    // struct term *answer;
    // int n_answer;
    // autocomplete(&answer, &n_answer, terms, nterms, "Tor");
    //free allocated blocks here -- not required for the project, but good practice
    return 0;
}