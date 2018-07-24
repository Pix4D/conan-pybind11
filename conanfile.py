from conans import ConanFile, CMake
from conans.tools import os_info
import os

class pybind11Conan(ConanFile):
    name = 'pybind11'
    lib_version = '2.2.3'
    revision = '1'
    version = '{}-{}'.format(lib_version, revision)
    settings = 'os', 'compiler', 'build_type', 'arch'
    description = 'Recipe for the official pybind11 repository'
    url = 'https://github.com/pybind/pybind11.git'
    license = 'BSD-like'

    def package_id(self):
        self.info.header_only()

    def source(self):
        self.run('git clone --depth 1 --branch v%s %s %s' % (self.lib_version, self.url, self.name))

    def build(self):
        cmake = CMake(self, parallel=True)
        cmake_args = {'PYBIND11_TEST': 'OFF'} # tests require pytest, which may not be available
        if not os_info.is_windows:
            cmake_args['PYBIND11_CPP_STANDARD'] = '-std=c++11'

        cmake.configure(source_dir=os.path.join('..',  self.name), build_dir='build', defs=cmake_args)
        cmake.build(target='install')
