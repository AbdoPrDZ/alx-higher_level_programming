#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: the head of the list
 * Return: 1 if it is a palindrome, 0 is not
 */
int is_palindrome(listint_t **head)
{
	listint_t *next, *nextNext, *node, *temp;
	next = *head;
	nextNext = *head;
	node = NULL;

	if (!*head || !(*head)->next)
		return (1);
	else
		while (nextNext && nextNext->next)
		{
			nextNext = nextNext->next->next;
			temp = next->next;
			next->next = node;
			node = next;
			next = temp;
		}

	if (nextNext)
		next = next->next;

	while (node && next)
	{
		if (node->n != next->n)
			return (0);

		node = node->next;
		next = next->next;
	}

	return (1);
}
