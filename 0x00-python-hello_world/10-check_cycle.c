#include "lists.h"


/**
 * check_cycle - check for cycles
 * @list: list to check
 * Return: 1 if it's a cycle 0 if not
 */


int check_cycle(listint_t *list)
{
	listint_t *tortoise, *hare;

	if (list == NULL || list->next == NULL)
		return (0);

	tortoise = list;
	hare = list->next;

	while (hare != NULL && hare->next != NULL && hare != tortoise)
	{
		tortoise = tortoise->next;
		hare = hare->next->next;
	}

	return (hare == tortoise);
}

