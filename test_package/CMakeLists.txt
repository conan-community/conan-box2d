project(test_package)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

message("LIBS: ${CONAN_LIBS}")

add_executable(test_package test_package.cpp)
target_link_libraries(test_package ${CONAN_LIBS})