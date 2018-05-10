from conans import ConanFile, CMake, tools
import os


class DocoptTestConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch", "cppstd"
    generators = "cmake"
    requires = "excel/1.1.4@igormironchik/stable"

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def imports(self):
        self.copy(pattern="*.dll", src="bin", dst="bin")
        self.copy(pattern="*.dylib", src="lib", dst="bin")

    def test(self):
        with tools.chdir("bin"):
            self.run(".%stest_package" % os.sep)