# Cpp-Project-Template

A C++ project template uses CMake with Doxygen, Sphinx integrated

## Used for

Two main things when starting a new Cpp project

- Dependency
- Documentation

And of course, a general purpose Cpp project structure

## Features

- **Package Management** using
  - [vcpkg github repo](https://github.com/microsoft/vcpkg)
  - [vcpkg buildsystem integration](https://vcpkg.readthedocs.io/en/latest/users/integration/)
- **Project Documentation** using
  - **[Doxygen](https://github.com/doxygen/doxygen)**
  - **[Sphynix](https://github.com/sphinx-doc/sphinx/)**
- **CMake Integratation**

## Prerequisite

Basically you just need [CMake](https://cmake.org) and a C++ compiler.

If you want to take the way provided by this repo, you also need

- [Python](https://www.python.org)
- [Doxygen](https://github.com/doxygen/doxygen)

## Installation

### Use this template

You can click the [Use this template](https://github.com/WilliamCodeBox/Cpp-Project-Template/generate) button to create your new Github repository

### Clone this repository

- clone this repository
  ```bash
  > git clone https://github.com/WilliamCodeBox/Cpp-Project-Template.git
  ```
- use the name of your greate Cpp project
  ```bash
  > mv Cpp-Project-Template NameOfYourCppProject
  ```
- start over the version control
  ```bash
  > cd NameOfYourCppProject
  > rm -rf .git
  > git init
  ```

## Usage

- Environment for documentation

  > **Suggestion**: create a virtural python environment using [conda](https://docs.conda.io/en/latest/)

  - [ ] **TODO**: may be a python/bash script to automatically run the following steps

  * install required python packages

    ```bash
    > cd docs
    > pip install -r requirements.txt
    ```

  - change relavent content within `config.json`

    - `project` = 'cpp-project-template'
    - `author` = 'WilliamCodeBox'
    - `release` = '1.0.0'
    - `sourceDir` = "../include"
    - `rootFileTitle` = "Library API"

  - Generate the docs

    ```bash
    > make html
    ```

- Third-party C++ libraries
  - search and install the libs with the help of `vcpkg`
    ```bash
    > ./vcpkg search gtest
    > ./vcpkg install gtest
    ```
  - find the libs within `CMakeLists.txt`

### Documentation Customization

[CMake Doxygen Config](https://cmake.org/cmake/help/latest/module/FindDoxygen.html)

## References and Thanks to

- [Clear, Functional C++ Documentation with Sphinx + Breathe + Doxygen + CMake](https://devblogs.microsoft.com/cppblog/clear-functional-c-documentation-with-sphinx-breathe-doxygen-cmake/)
- [Adding doxygen support to CMakeLists.txt](http://www.miscdebris.net/blog/2019/02/25/adding-doxygen-support-to-cmakelists-txt/)
- [David/CMakeTemplate](https://github.com/DavidAce/CMakeTemplate)
- [vcpkg](https://github.com/microsoft/vcpkg)
