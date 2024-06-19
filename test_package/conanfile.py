import os
import sys

from conans import ConanFile, CMake


class Pybind11TestConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def test(self):
        module_path = os.path.join(self.source_folder, "test.py")
        self.run(f'{sys.executable} "{module_path}"')
