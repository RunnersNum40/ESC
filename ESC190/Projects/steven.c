#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

#include "autocomplete.h"

#define MAXLINE 200

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


int down (struct term *terms, int mid, char *substr) {
    if (mid <= 0 || mstrcmp(terms[mid-1].term, substr) != 0) {
        return mid;
    }
    else {
        return down(terms, mid-1, substr);
    }
}

int up (struct term *terms, int mid, char *substr, int nterms) {
    if (mid >= nterms || mstrcmp(terms[mid+1].term, substr) != 0) {
        return mid;
    }
    else {
        return up(terms, mid+1, substr, nterms);
    }
}

int reals(struct term *terms, int starter, int nterms, char *substr) {
    if (starter < nterms) {
        int mid;
        mid = (nterms + starter)/2;
        if (mstrcmp(terms[mid].term, substr) == 0) {
            return up(terms, mid, substr, nterms);
        }
        if (mstrcmp(terms[mid].term, substr) < 0) {
            return reals(terms, starter, mid-1, substr);
        }
        if (mstrcmp(terms[mid].term, substr) > 0) {
            return reals(terms, mid+1, nterms, substr);
        }
    }
    else {
        return -1;
    }
}

int real(struct term *terms, int starter, int nterms, char *substr) {
    if (starter < nterms) {
        int mid;
        mid = (nterms + starter)/2;
        if (mstrcmp(terms[mid].term, substr) == 0) {
            return down(terms, mid, substr);
        }
        if (mstrcmp(terms[mid].term, substr) < 0) {
            return real(terms, starter, mid-1, substr);
        }
        if (mstrcmp(terms[mid].term, substr) > 0) {
            return real(terms, mid+1, nterms, substr);
        }
    }
    else {
        return -1;
    }
}

int lowest_match(struct term *terms, int nterms, char *substr) {
    int a= 0;
    return real(terms, a, nterms, substr);
}

int highest_match(struct term *terms, int nterms, char *substr) {
    int a= 0;
    return reals(terms, a, nterms, substr);
}

int compare(struct term term1, struct term term2) {
    return mstrcmp(term1.term, term2.term);
}

void autocomplete(struct term **answer, int *n_answer, struct term *terms, int nterms, char *substr) {
    int a, b, i, c;
    a = lowest_match(terms, nterms, substr);
    b = highest_match(terms, nterms, substr);
    i = 0;
    c = b-a;
    struct term** stupid = &terms;
    for (int i =0; i <= c; i++) {
        answer[i]->weight = stupid[i+a]->weight;
        strcpy(answer[i]->term, stupid[i+a]->term);
    }
    qsort(answer, c, sizeof(struct term), compare);
}

int main(void) {
    struct term *terms;
    int nterms;
    read_in_terms(&terms, &nterms, "cities.txt");
    printf("%d\n", nterms);
    lowest_match(terms, nterms, "Tor");
    highest_match(terms, nterms, "Tor");
    
    struct term *answer;
    int n_answer;
    autocomplete(&answer, &n_answer, terms, nterms, "Tor");
    //free allocated blocks here -- not required for the project, but good practice
    return 0;
}