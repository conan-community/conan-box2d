cmake_minimum_required(VERSION 3.1.3)

project(cmake_wrapper)

set (CMAKE_CXX_STANDARD 11)
set (CMAKE_CXX_STANDARD_REQUIRED ON)

include(conanbuildinfo.cmake)
conan_basic_setup()

set(BOX2D_SOURCE_DIR ${CMAKE_CURRENT_SOURCE_DIR}/sources/Box2D )
SET(CMAKE_INSTALL_MESSAGE ALWAYS)


option(BOX2D_INSTALL "Install Box2D libs, includes, and CMake scripts" ${BOX2D_INSTALL_BY_DEFAULT})
option(BOX2D_BUILD_SHARED "Build Box2D shared libraries" OFF)
option(BOX2D_BUILD_STATIC "Build Box2D static libraries" ON)

set(BOX2D_VERSION 2.3.2)
set(LIB_INSTALL_DIR lib${LIB_SUFFIX})

file (GLOB BOX2D_Collision_SRCS
	LIST_DIRECTORIES false
	${BOX2D_SOURCE_DIR}/Collision/*.cpp)

file (GLOB BOX2D_Collision_HDRS
	LIST_DIRECTORIES false
	${BOX2D_SOURCE_DIR}/Collision/*.h)

file (GLOB BOX2D_Shapes_SRCS
	LIST_DIRECTORIES false
	${BOX2D_SOURCE_DIR}/Collision/Shapes/*.cpp)

file (GLOB BOX2D_Shapes_HDRS
	LIST_DIRECTORIES false
	${BOX2D_SOURCE_DIR}/Collision/Shapes/*.h)

file (GLOB BOX2D_Common_SRCS
	LIST_DIRECTORIES false
	${BOX2D_SOURCE_DIR}/Common/*.cpp)

file (GLOB BOX2D_Common_HDRS
	LIST_DIRECTORIES false
	${BOX2D_SOURCE_DIR}/Common/*.h)

file (GLOB BOX2D_Dynamics_SRCS
	LIST_DIRECTORIES false
	${BOX2D_SOURCE_DIR}/Dynamics/*.cpp)

file (GLOB BOX2D_Dynamics_HDRS
	LIST_DIRECTORIES false
	${BOX2D_SOURCE_DIR}/Dynamics/*.h)

file (GLOB BOX2D_Contacts_SRCS
	LIST_DIRECTORIES false
	${BOX2D_SOURCE_DIR}/Dynamics/Contacts/*.cpp)

file (GLOB BOX2D_Contacts_HDRS
	LIST_DIRECTORIES false
	${BOX2D_SOURCE_DIR}/Dynamics/Contacts/*.h)

file (GLOB BOX2D_Joints_SRCS
	LIST_DIRECTORIES false
	${BOX2D_SOURCE_DIR}/Dynamics/Joints/*.cpp)

file (GLOB BOX2D_Joints_HDRS
	LIST_DIRECTORIES false
	${BOX2D_SOURCE_DIR}/Dynamics/Joints/*.h)

file(GLOB BOX2D_Rope_SRCS
	LIST_DIRECTORIES false
	${BOX2D_SOURCE_DIR}/Rope/*.cpp
)

file(GLOB BOX2D_Rope_HDRS
	LIST_DIRECTORIES false
	${BOX2D_SOURCE_DIR}/Rope/*.h
)

file(GLOB BOX2D_General_HDRS
	LIST_DIRECTORIES false
	${BOX2D_SOURCE_DIR}/*.h
)

include_directories( ${BOX2D_SOURCE_DIR}/../ )

if(BOX2D_BUILD_SHARED)
	add_library(Box2D_shared SHARED
		${BOX2D_General_HDRS}
		${BOX2D_Joints_SRCS}
		${BOX2D_Joints_HDRS}
		${BOX2D_Contacts_SRCS}
		${BOX2D_Contacts_HDRS}
		${BOX2D_Dynamics_SRCS}
		${BOX2D_Dynamics_HDRS}
		${BOX2D_Common_SRCS}
		${BOX2D_Common_HDRS}
		${BOX2D_Shapes_SRCS}
		${BOX2D_Shapes_HDRS}
		${BOX2D_Collision_SRCS}
		${BOX2D_Collision_HDRS}
		${BOX2D_Rope_SRCS}
		${BOX2D_Rope_HDRS}
	)
	set_target_properties(Box2D_shared PROPERTIES
		OUTPUT_NAME "Box2D"
		CLEAN_DIRECT_OUTPUT 1
		VERSION ${BOX2D_VERSION}
	)
endif()

if(BOX2D_BUILD_STATIC)
	add_library(Box2D STATIC
		${BOX2D_General_HDRS}
		${BOX2D_Joints_SRCS}
		${BOX2D_Joints_HDRS}
		${BOX2D_Contacts_SRCS}
		${BOX2D_Contacts_HDRS}
		${BOX2D_Dynamics_SRCS}
		${BOX2D_Dynamics_HDRS}
		${BOX2D_Common_SRCS}
		${BOX2D_Common_HDRS}
		${BOX2D_Shapes_SRCS}
		${BOX2D_Shapes_HDRS}
		${BOX2D_Collision_SRCS}
		${BOX2D_Collision_HDRS}
		${BOX2D_Rope_SRCS}
		${BOX2D_Rope_HDRS}
	)
	set_target_properties(Box2D PROPERTIES
		CLEAN_DIRECT_OUTPUT 1
		VERSION ${BOX2D_VERSION}
	)
endif()

if(BOX2D_INSTALL)
	file(COPY ${BOX2D_General_HDRS} DESTINATION ${CMAKE_CURRENT_SOURCE_DIR}/include/Box2D)
	file(COPY ${BOX2D_Collision_HDRS} DESTINATION include/Box2D/Collision)
	file(COPY ${BOX2D_Shapes_HDRS} DESTINATION include/Box2D/Collision/Shapes)
	file(COPY ${BOX2D_Common_HDRS} DESTINATION include/Box2D/Common)
	file(COPY ${BOX2D_Dynamics_HDRS} DESTINATION include/Box2D/Dynamics)
	file(COPY ${BOX2D_Contacts_HDRS} DESTINATION include/Box2D/Dynamics/Contacts)
	file(COPY ${BOX2D_Joints_HDRS} DESTINATION include/Box2D/Dynamics/Joints)
	file(COPY ${BOX2D_Rope_HDRS} DESTINATION include/Box2D/Rope)

	# install libraries
	if(BOX2D_BUILD_SHARED)
		install(TARGETS Box2D_shared EXPORT Box2D-targets
				LIBRARY DESTINATION ${LIB_INSTALL_DIR}
				ARCHIVE DESTINATION ${LIB_INSTALL_DIR}
				RUNTIME DESTINATION bin)
	endif()
	if(BOX2D_BUILD_STATIC)
		install(TARGETS Box2D EXPORT Box2D-targets DESTINATION ${LIB_INSTALL_DIR})
	endif()
endif(BOX2D_INSTALL)
