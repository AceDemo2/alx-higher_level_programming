#include "lists.h"
/**
 * is_palindrome - Checks if a singly linked list is a palindrome
 * @head: Pointer to the head of the list
 *
 * Return: 1 if the list is a palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	listint_t *i = *head, *j, *h2, *m = NULL, *n = NULL;
	int k = 0, l = 1;
	if (!*head)
		return(1);
	while (i)
	{
		i = i->next;
		k++;
	}
	i = *head;
	while (l < k / 2)
	{
		i = i->next;
		l++;
	}
	if (k % 2 == 1)
		i = i->next;
	h2 = i->next;
	i = *head;
	while (h2)
	{
		m = h2->next;
		h2->next = n;
		n = h2;
		h2 = m;
	}
	h2 = n;
	j = h2;
	while (i)
	{
		if (i->n == j->n)
		{
			i = i->next;
			j = j->next;
		}
		else
			return (0);
	}
	return (1);
}
