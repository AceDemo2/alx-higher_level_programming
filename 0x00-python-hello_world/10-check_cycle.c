#include "lists.h"
/**
 * check_cycle - check for loop in LL
 * @list: head of linked list
 *
 * Description - check for loops in LL
 * Return: 1 if cycled, 0 if not
 */
int check_cycle(listint_t *list)
{
	listint_t *i = list, *j = list;
	if (!list)
		return (0);
	while (i && i->next)
	{
		j = j->next;
		i = i->next->next;
		if (i == j)
			return (1);
	}
	return (0);
}
