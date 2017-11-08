#include <pybind11/pybind11.h>

int add(int i, int j) {
    return i + j;
}

namespace py = pybind11;

PYBIND11_MODULE(examplemodule, m) {
    m.doc() = "some module description";
    m.def("addNumbers", &add, "A function to add two numbers");
}
