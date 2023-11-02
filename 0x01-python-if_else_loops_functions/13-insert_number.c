#include "lists.h"
#include <stdlib.h>
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *ptr, *new, *temp = NULL;
	int x;

	if (head == NULL)
		return (NULL);
	if (*head == NULL)
	{
		new = malloc(sizeof(listint_t));
		if (new == NULL)
			return NULL;
		new->n = number;
		new->next = NULL;
		*head = new;
		return (*head);
	}
	ptr = *head;
	while (*head)
	{
		if (ptr->n > number)
		{
			x = ptr->n;
			ptr->next = temp;
			ptr->n = number;
			new = malloc(sizeof(listint_t));
			if (new == NULL)
				return NULL;
			ptr->next = new;
			new->n = x;
			new->next = temp;
			break;
		}
		ptr = ptr->next;
	}
	return (*head);
	
}
