#include "lists.h"

/**
 * check_cycle - checks if a single list has a cycle in there
 * @list: linked list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *node = list;
	listint_t *next = list;

	if (!list)
		return (0);

	while (node && next && next->next)
	{
		node = node->next;
		next = next->next->next;
		if (node == next)
			return (1);
	}

	return (0);
}
