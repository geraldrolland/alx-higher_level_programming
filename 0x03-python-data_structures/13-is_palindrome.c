#include <stdlib.h>
#include "lists.h"
/**
 *is_palindrome - checks if singly linked is a palidrome
 *@head: pointer to the head pointer of a list
 *Return: 1 on success or 0 on failure
 */
int is_palindrome(listint_t **head)
{
	listint_t *ptr = *head;
	int first_num;

	if (*head == NULL || head == NULL)
		return (1);
	first_num = ptr->n;
	while (ptr->next == NULL)
		ptr = ptr->next;
	if (ptr->n == first_num)
		return (1);
	return (0);

}
