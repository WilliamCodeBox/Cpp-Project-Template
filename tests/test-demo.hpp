#if !defined(CPP_PROJECT_TEMPLATE_TEST_DEMO_H)
#define CPP_PROJECT_TEMPLATE_TEST_DEMO_H

#include <gtest/gtest.h>

#include "demo.hpp"

TEST(CppProjectTemplate, demo) { ASSERT_EQ(demo::add(1, 1), 2.0); }

#endif  // CPP_PROJECT_TEMPLATE_TEST_DEMO_H
