#include<stdio.h>
#include<stdlib.h>

struct node
{
	int data;
	struct node* next;
};

void traverse(struct node* start)
{
	while(start!=NULL)
	{	
		printf("\n %d \n", start -> data);
		start = start -> next;
	}
}

int main()
{
	int a,b,c;
	struct node* temp = NULL;
	struct node* first = NULL;
	struct node* second = NULL;
	struct node* third = NULL;


	first = (struct node*)malloc(sizeof(struct node));
	second = (struct node*)malloc(sizeof(struct node));
	third = (struct node*)malloc(sizeof(struct node));


	first -> data = 1;
	first -> next = second;

	second -> data = 2;
	second -> next = third;

	third -> data = 3;
	third -> next = temp;

	
	traverse(first);
	return 0;
}