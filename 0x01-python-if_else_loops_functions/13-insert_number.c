#include <stdlib.h>
#include <stdio.h>
#include "lists.h"

/**
 * insert_node - function: insert a number in  a linked list
 * @head:  head of the linked lists
 * @number: digit or number to insert
 *
 * Return: NULL if fail 
 *         Else node.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;

	if (node == NULL || node->n >= number)
	{
		new->next = node;
		*head = new;
		return (new);
	}

	while (node && node->next && node->next->n < number)
		node = node->next;

	new->next = node->next;
	node->next = new;

	return (new);
}
