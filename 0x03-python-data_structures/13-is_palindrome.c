#include <stdlib.h>
#include "lists.h"
/**
 * is_palindrome - checks if singly linked list is a palindrome
 * @head: pointer to the head pointer of a list
 * Return: 1 if it's a palindrome, 0 if not
 */
int is_palindrome(listint_t **head)
{
	listint_t *ptr = *head;
	int values[4096];
	int count = 0, i;

	if (*head == NULL || head == NULL)
		return (1);
	while (ptr != NULL)
	{
		values[count] = ptr->n;
		ptr = ptr->next;
		count++;
	}
	for (i = 0; i < count / 2; i++)
	{
		if (values[i] != values[count - i - 1])
			return (0);
	}
	return (1);
}
