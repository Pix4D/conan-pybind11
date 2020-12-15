from conans import ConanFile, tools, CMake


class PyBind11Conan(ConanFile):
    name = "pybind11"
    upstream_version = "2.6.1"
    revision = "0"
    version = "{}-{}".format(upstream_version, revision)
    settings = "os", "compiler", "arch", "build_type"
    description = "Seamless operability between C++11 and Python"
    homepage = "https://github.com/pybind/pybind11"
    license = "BSD Style: https://github.com/pybind/pybind11/blob/master/LICENSE"
    url = "https://github.com/conan-community/conan-pybind11"
    no_copy_sources = True

    def source(self):
        tools.get("%s/archive/v%s.tar.gz" % (self.homepage, self.upstream_version))

    def build(self):
        cmake = CMake(self)
        cmake.definitions["PYBIND11_TEST"] = False
        cmake.configure(source_folder="pybind11-%s" % self.upstream_version)
        cmake.build()
        cmake.install()

    def package(self):
        self.copy("*LICENSE", keep_path=False)

    def package_id(self):
        # Make all options and dependencies (direct and transitive) contribute
        # to the package id
        self.info.requires.full_package_mode()
