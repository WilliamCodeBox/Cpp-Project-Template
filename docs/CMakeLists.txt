find_package(Doxygen)

if(DOXYGEN_FOUND)
    # things that you don't want to be documented
    set(DOXYGEN_EXCLUDE_PATTERNS )
    # project level info
    set(DOXYGEN_PROJECT_BRIEF "A Cpp project template uses CMake with Doxygen, Sphynix integrated.")


    # Some of Doxygen’s defaults are overridden 
    # to provide more appropriate behavior for a CMake project
    set(DOXYGEN_SOURCE_BROWSER YES)
    set(DOXYGEN_EXTRACT_PRIVATE YES)
    set(DOXYGEN_OUTPUT_DIRECTORY "${PROJECT_SOURCE_DIR}/docs/docs/doxygen")

    doxygen_add_docs(
        doxygen ALL
        ${PROJECT_SOURCE_DIR}
        COMMENT "Generating API docs"
    )
endif(DOXYGEN_FOUND)
