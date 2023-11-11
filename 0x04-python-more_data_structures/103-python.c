#include <Python.h>
/**
 *print_python - print python list
 *@p: variable
 *Return: void
 */

void print_python_list(PyObject *p) {
	Py_ssize_t size, i;
	PyObject *item;

	if (!PyList_Check(p)) {
		printf("  [ERROR] Invalid List Object\n");
		return;
	}

	size = PyList_Size(p);

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < size; ++i) {
		item = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
	}
}
/**
 *print_python_bytes - print python bytes
 *@p: variable
 *Return: void
 */

void print_python_bytes(PyObject *p) {
	Py_ssize_t size, i;
	char *bytes_str;

	if (!PyBytes_Check(p)) {
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = PyBytes_Size(p);
	bytes_str = PyBytes_AsString(p);

	printf("[.] bytes object info\n");
	printf("  [.] Size: %ld\n", size);
	printf("  [.] trying string: %s\n", bytes_str);

	if (size > 10)
		size = 10;

	printf("  [.] first %ld bytes: ", size);
	for (i = 0; i < size; ++i) {
		printf("%02hhx", bytes_str[i]);
		if (i < size - 1)
			printf(" ");
	}
	printf("\n");
}
