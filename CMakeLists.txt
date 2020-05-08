#################################################################
###                         Project                           ###
#################################################################
cmake_minimum_required(VERSION 3.7)
project               (YourGreatProjectName VERSION 1.0.0 LANGUAGES CXX)

#################################################################
###                         Guards                            ###
#################################################################
if(${CMAKE_SOURCE_DIR} STREQUAL ${CMAKE_BINARY_DIR})
    message(WARNING "In-source build detected")
    message(STATUS "Out-of-source build is preferred")
    message(STATUS "   Create a separate directory, named `build` for convention")
    message(STATUS "   and run CMake again")
endif()


#################################################################
###                         Options                           ###
#################################################################
set(BUILD_TESTS "Build the tests" OFF)
set(BUILD_DOCS "Build the docs" OFF)

#################################################################
###                       Dependencies                        ###
#################################################################
include   (cmake/HunterGate.cmake)
HunterGate(
    URL "https://github.com/cpp-pm/hunter/archive/v0.23.253.tar.gz"
    SHA1 "88ea6d37c897a81a080eb9ae0f69d7807bbb3c73")



#################################################################
###                         Sources                           ###
#################################################################
set(
    LIB_DEMO_SOURCE_FILES
    ${PROJECT_SOURCE_DIR}/source/demo.cpp)


#################################################################
###                         Targets                           ###
#################################################################
set                       (PROJECT_INCLUDE_DIR ${PROJECT_SOURCE_DIR}/include)
add_library               (demo SHARED ${LIB_DEMO_SOURCE_FILES})
target_include_directories(demo PUBLIC ${PROJECT_INCLUDE_DIR})
set_target_properties     (demo PROPERTIES CXX_STANDARD 11)


#################################################################
###                        Install                            ###
#################################################################



#################################################################
###                          Docs                             ###
#################################################################
if(BUILD_DOCS)
    add_subdirectory(docs)
endif()


#################################################################
###                          Tests                            ###
#################################################################
if(BUILD_TESTS)
    add_subdirectory(test)
endif()

