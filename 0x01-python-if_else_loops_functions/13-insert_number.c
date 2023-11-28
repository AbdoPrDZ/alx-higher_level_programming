#include "lists.h"

/**
 * insert_node - insert node into linked list
 * @head: the head of linked list
 * @number: The number want to insert
 * Return: NULL if fails or the new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node, *new;

	node = *head;
	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);

	new->n = number;

	if (!node || node->n >= number)
	{
		new->next = node;
		*head = new;
	}
	else
	{
		while (node && node->next && node->next->n < number)
			node = node->next;

		new->next = node->next;
		node->next = new;
	}

	return (new);
}
