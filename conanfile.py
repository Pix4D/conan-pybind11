from conans import ConanFile, CMake
from conans.tools import os_info

class pybind11Conan(ConanFile):
    name = 'pybind11'
    lib_version = '2.2'
    revision = '0'
    version = '{}-{}'.format(lib_version, revision)
    settings = 'os', 'compiler', 'build_type', 'arch'
    description = 'Recipe for the official pybind11 repository'
    url = 'https://github.com/pybind/pybind11.git'
    license = 'BSD-like'

    def package_id(self):
        self.info.header_only()

    def config_options(self):
        self.requires('Eigen3/3.3.3-3@pix4d/stable')

    def source(self):
        self.run('git clone --depth 1 --branch v%s %s %s' % (self.lib_version, self.url, self.name))

    def build(self):
        cmake = CMake(self, parallel=True)
        cmake_args = {}
        cmake_args['PYBIND11_TEST'] = 'OFF' # tests require pytest, which may not be available
        if not os_info.is_windows:
            cmake_args['PYBIND11_CPP_STANDARD'] = '-std=c++11'

        cmake.configure(source_dir='../%s' % self.name, build_dir='build', defs=cmake_args)
        cmake.build(target='install')
