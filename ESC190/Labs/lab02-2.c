#include <stdio.h>
#include <stdlib.h>

struct node{
    void *p_data; //a pointer to data (allocated with malloc)
    int type; // 0 if int, 1 if float, 2 if double
    struct node *next;
};

void print(struct node* loc) {
    while (loc->next != NULL) {
        if(loc->type==0) {
          printf("%d, ", *(int*)(loc->p_data));
        }
        else if(loc->type==1) {
          printf("%f, ", *(float*)(loc->p_data));
        }
        else if(loc->type==2) {
          printf("%lf, ",  *(double*)(loc->p_data));
        }
        loc = loc->next; 
    }
    if(loc->type==0) {
        printf("%d", *(int*)(loc->p_data));
      }
      else if(loc->type==1) {
        printf("%f", *(float*)(loc->p_data));
      }
      else if(loc->type==2) {
        printf("%lf",  *(double*)(loc->p_data));
    }
    printf("\n");
}

struct node* append(void* p_data, int type, struct node* head) {
    while(head->next != NULL) {
      head = head->next;
    }
    struct node *node = (struct node *)malloc(sizeof(struct node));
    node->type = type;
    node->p_data = p_data;
    node->next = NULL;

    head->next = node;

    return node;
}

void append_int(int n, struct node* head) {
     void* data = (int*)malloc(sizeof(int));
    *(int*)data = n;
    append(data, 0, head);
}

void append_float(float n, struct node* head) {
    void* data = (float*)malloc(sizeof(float));
    *(float*)data = n;
    append(data, 1, head);
}

void append_double(double n, struct node* head) {
    void* data = (double*)malloc(sizeof(double));
    *(double*)data = n;
    append(data, 2, head);
}

struct node* new(void* p_data, int type) {
    struct node *node = (struct node *)malloc(sizeof(struct node));
    node->type = type;
    node->p_data = p_data;
    node->next = NULL;

    return node;
}

int main() {
  int* data = (int*) malloc(sizeof(int));
  *data = 384;
  struct node* head = new(data, 0);
  append_double(2389374.38744, head);
  append_float(7.38744, head);
  append_int(2389374.38744, head);
  print(head);
}