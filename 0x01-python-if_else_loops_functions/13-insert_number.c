#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: double pointer to the head of the list
 * @number: the number to insert
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
    listint_t *new, *current, *prev;

    if (!head)
        return (NULL);

    new = malloc(sizeof(listint_t));
    if (!new)
        return (NULL);
    new->n = number;
    new->next = NULL;

    if (!*head || (*head)->n >= number) {
        new->next = *head;
        *head = new;
        return (new);
    }

    prev = NULL;
    current = *head;

    while (current && current->n < number) {
        prev = current;
        current = current->next;
    }

    prev->next = new;
    new->next = current;

    return (new);
}

