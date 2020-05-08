enable_testing()

hunter_add_package(GTest)
find_package      (GTest REQUIRED)

add_executable            (demoTest test-main.cpp)
target_include_directories(
                           demoTest PRIVATE 
                           ${CMAKE_CURRENT_SOURCE_DIR} 
                           ${PROJECT_INCLUDE_DIR} 
                           ${GTEST_INCLUDE_DIRS})
target_link_libraries    (demoTest PRIVATE demo GTest::GTest GTest::Main)
set_target_properties    (demoTest PROPERTIES CXX_STANDARD 11)

add_test(NAME demoTest COMMAND demoTest)