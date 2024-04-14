size_t print_dlistint(const dlistint_t *h)
{
	int i = 0;
	dlistint_t *j = h;

	while (j)
	{
		printf("%d\n", j->n);
		i++;
		j = j->next;
	}
	return (i);

