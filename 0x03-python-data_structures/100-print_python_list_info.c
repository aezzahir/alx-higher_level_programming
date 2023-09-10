#include <Python.h>

/**
 * print_python_list_info - prints basic info about Python lists
 * @p: PyObject list
 */
void print_python_list_info(PyObject *p)
{
    int size, alloc, i;
    PyObject *item;

    /* Check if p is a list */
    if (PyList_Check(p))
    {
        size = PyList_Size(p);
        alloc = ((PyListObject *)p)->allocated;

        printf("[*] Size of the Python List = %d\n", size);
        printf("[*] Allocated = %d\n", alloc);

        /* Iterate through list items and print their types */
        for (i = 0; i < size; i++)
        {
            item = PyList_GetItem(p, i);
            printf("Element %d: %s\n", i, Py_TYPE(item)->tp_name);
        }
    }
}
