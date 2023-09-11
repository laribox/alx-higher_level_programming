#include <Python.h>
#include <stdio.h>
#include <stdlib.h>

/**
 * print_python_list_info - Print basic info about Python
 * @p: PyObject
 * Return: Nothing
 */

void print_python_list_info(PyObject *p)
{
    PyObject *item;
    PyList *list = (PyList *)p;
    int x, size, alloc;

    size = Py_SIZE(p);
    alloc = list->allocated;
    printf("[*] Size of the Python List = %d\n", size);
    printf("[*] Allocated = %d\n", alloc);

    for (x = 0; x < size; x++)
    {
        item =  PyList_GetItem(p, x);
        printf("Element %d: %s\n", x, Py_TYPE(item)->tp_name);
    }
}
