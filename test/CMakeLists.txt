enable_testing()

find_package              (Gtest CONFIG REQUIRED)
add_executable            (demoTest test-main.cpp)
target_include_directories(
                           demoTest PRIVATE 
                           ${CMAKE_CURRENT_SOURCE_DIR} 
                           ${PROJECT_INCLUDE_DIR} 
                           ${GTEST_INCLUDE_DIRS})
target_link_libraries     (demoTest PRIVATE demo GTest::gtest GTest::gtest_main GTest::gmock GTest::gmock_main)
set_target_properties     (demoTest PROPERTIES CXX_STANDARD 11)

add_test(NAME demoTest COMMAND demoTest)