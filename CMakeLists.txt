#################################################################
###                         Options                           ###
#################################################################
option(BUILD_TESTS "Build the tests" ON)
option(BUILD_EXPERIMENTS, "Build the experiments" ON)
option(CMAKE_MODULE_PATH "${PROJECT_SOURCE_DIR}/cmake" ${CMAKE_MODULE_PATH})

#################################################################
###                          vcpkg                            ###
#################################################################
if(DEFINED ENV{VCPKG_ROOT} AND NOT DEFINED CMAKE_TOOLCHAIN_FILE)
  set(CMAKE_TOOLCHAIN_FILE "$ENV{VCPKG_ROOT}/scripts/buildsystems/vcpkg.cmake"
      CACHE STRING "")
endif()

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
###                       Dependencies                        ###
#################################################################




#################################################################
###                         Sources                           ###
#################################################################
set(LIB_DEMO_SOURCE_FILES
    ${PROJECT_SOURCE_DIR}/src/demo.cpp)


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
###                       Subfolders                          ###
#################################################################
if(BUILD_EXPERIMENTS)
    add_subdirectory(experiments)
endif()
if(BUILD_TESTS)
    add_subdirectory(tests)
endif()

