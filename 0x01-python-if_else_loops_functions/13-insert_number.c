#include "lists.h"
/**
 * insert_node - Inserts a number into a sorted singly-linked list.
 * @head: A pointer the head of the linked list.
 * @number: The number to insert.
 * Return: 0 If the function fails or pointer to the new node.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *i = *head, *j, *k = *head;
    
	j = malloc(sizeof(listint_t));
	if (j == NULL)
		return (NULL);
	j->n = number;
	if (!*head || i->n >= number)
	{
		j->next = *head;
		*head = j;
		return (j);
	}
	i = i->next;
	while (i && i->n < number)
	{
		i = i->next;
		k = k->next;
	}
	j->next = i;
	k->next = j;
	return (j);
}
