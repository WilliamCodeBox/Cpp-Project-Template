#include "gtest/gtest.h"
#include "test-demo.hpp"

int main(int argc, char *argv[]) {
    ::testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}
