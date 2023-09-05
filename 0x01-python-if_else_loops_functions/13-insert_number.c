#include "lists.h"

/**
 * insert_node - 
 */


listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *tmp = *head;

	new->n = number;
	new->next = NULL;

	if (*tmp == NULL)
		*head = new;

	while(*tmp != NULL)
	{
		if(number < tmp->n)
			tmp = tmp->next;
		else
		{
			new->next = temp->next->next;
			temp->next = new;
		}	

	}
	return *head;
}
