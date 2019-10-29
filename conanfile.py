import os
from conans import ConanFile, CMake, tools


class Box2dConan(ConanFile):
    name = "box2d"
    version = "2.3.2.ef96a4f"
    license = "Zlib"
    description = "Box2D is a 2D physics engine for games"
    homepage = "http://box2d.org/"
    url = "https://github.com/conan-community/conan-box2d"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False],
               "fPIC": [True, False]}
    default_options = "shared=False", "fPIC=True"
    generators = "cmake"
    exports = "LICENSE"
    exports_sources = "CMakeLists.txt"
    revision_mode = "scm"
    scm = {
        "type": "git",
        "subfolder": "sources",
        "url": "https://github.com/erincatto/Box2D.git",
        "revision": version.split(".")[-1],
     }

    def config_options(self):
        if self.settings.os == "Windows":
            del self.options.fPIC

    def build(self):
        cmake = CMake(self)
        cmake.definitions["BOX2D_BUILD_SHARED"] = self.options.shared
        cmake.definitions["BOX2D_BUILD_STATIC"] = not self.options.shared
        if self.settings.os == "Windows" and self.options.shared:
            cmake.definitions["CMAKE_WINDOWS_EXPORT_ALL_SYMBOLS"] = True
        cmake.definitions["BOX2D_INSTALL"] = True
        cmake.configure()
        cmake.build()

    def package(self):
        self.copy("LICENSE", dst="licenses", src=self.scm["subfolder"])
        self.copy("*", dst="include/Box2D", src="include/Box2D")
        self.copy("*.lib", dst="lib", src="lib", keep_path=False)
        self.copy("*.pdb", dst="lib", src="lib", keep_path=False)
        self.copy("*.dll", dst="bin", src="bin", keep_path=False)
        self.copy("*.pdb", dst="bin", src="bin", keep_path=False)
        self.copy("*.so*", dst="lib", keep_path=False, symlinks=True)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["Box2D"]
