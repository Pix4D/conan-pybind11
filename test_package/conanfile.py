from conans import ConanFile, CMake
import os
import sys

class pybind11TestConan(ConanFile):
    settings = 'os', 'compiler', 'build_type', 'arch'
    generators = 'cmake'

    def build(self):
        cmake = CMake(self)
        cmake_args = {'PYTHON_EXECUTABLE': sys.executable} # set python version same as conan venv

        cmake.configure(source_dir=self.conanfile_directory, defs=cmake_args)
        cmake.build()

    def test(self):
        # make sure python can find the libraries
        lib_path = os.path.join(self.build_folder, "lib")
        sys.path.append(lib_path)

        import examplemodule
        assert examplemodule.addNumbers(2,3) == 5
