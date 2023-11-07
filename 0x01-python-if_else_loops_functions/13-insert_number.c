#include "lists.h"
#include <stdlib.h>

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *ptr, *new, *temp;

	if (head == NULL)
		return (NULL);

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	if (*head == NULL || number < (*head)->n)
	{
		new->next = *head;
		*head = new;
		return (new);
	}
	ptr = *head;
	temp = NULL;
	while (ptr)
	{
		if (ptr->n > number)
		{
			new->next = ptr;
			temp->next = new;
			return (new);
		}
		temp = ptr;
		ptr = ptr->next;
	}
	temp->next = new;
	new->next = NULL;
	return (new);
}
