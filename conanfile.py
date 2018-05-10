from conans import ConanFile, CMake, tools
import os
import shutil

class Box2dConan(ConanFile):
    name = "box2d"
    version = "2.3.1"
    license = "Zlib"
    description = "Box2D is a 2D physics engine for games"
    homepage = "http://box2d.org/"
    url = "https://github.com/conan-community/conan-box2d"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    generators = "cmake"
    exports = "LICENSE"

    @property
    def source_subfolder(self):
        return "sources"

    def source(self):
        tools.get("https://github.com/erincatto/Box2D/archive/v%s.zip" % self.version)
        os.rename("Box2D-%s" % self.version, self.source_subfolder)

    def build(self):
        cmake = CMake(self)
        cmake.definitions["BOX2D_BUILD_SHARED"] = self.options.shared
        cmake.definitions["BOX2D_BUILD_STATIC"] = not self.options.shared
        cmake.definitions["BOX2D_BUILD_EXAMPLES"] = False
        cmake.configure(source_folder="%s/Box2D" % self.source_subfolder)
        cmake.build()

    def package(self):
        self.copy("License.txt", dst="licenses", src="%s/Box2D" % self.source_subfolder)
        self.copy("*.h", dst="include/Box2D", src="%s/Box2D/Box2D" % self.source_subfolder)
        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)
