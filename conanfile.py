from conans import ConanFile
from conans import tools

class CxxoptsConan(ConanFile):
    name = "cxxopts"
    version = "2.0.0"
    description = "Lightweight C++ command line option parser."
    license = "MIT"
    url = "https://github.com/jarro2783/cxxopts"
    exports_sources = "include/*"
    no_copy_source = True

    def package(self):
        self.copy(pattern="*.hpp", src="include", dst="include/cxxopts")

    def package_id(self):
        self.info.header_only()
