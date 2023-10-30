#include "lists.h"
/**
 * check_cycle - check cycle in a linked list
 * @list: pointer to the head node
 * Return: 0 on success, 1 on failure
 */
int check_cycle(listint_t *list)
{
	listint_t *fast = NULL;
	listint_t *slow = NULL;

	if (list == NULL || list->next == NULL)
		return (0);
	fast = (list->next)->next;
	slow = list->next;
	while (slow != NULL && fast != NULL && fast->next != NULL)
	{
		if (fast == slow)
			return (1);
		fast = (fast->next)->next;
		slow = slow->next;
	}
	return (0);
}
