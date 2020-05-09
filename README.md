# Cpp-Project-Template

A C++ project template uses CMake with Doxygen, Sphinx integrated

## Used for

Two main things when starting a new Cpp project

- Dependency
- Documentation
- And of course, a general purpose Cpp project structure

## Features

- **Package Management** using
  - [Hunter](https://hunter.readthedocs.io/en/latest/index.html).
- **Project Documentation** using
  - **[Doxygen](https://github.com/doxygen/doxygen)**
  - **[Sphynix](https://github.com/sphinx-doc/sphinx/)**
- **CMake Integratation**

## Prerequisite

- CMake
- Doxygen

## Usage

### Use this template

You can click the `Use this template` button to create your new Github repository

![Use this template](./images/use-this-template.png)

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

## References and Thanks to

- [Clear, Functional C++ Documentation with Sphinx + Breathe + Doxygen + CMake](https://devblogs.microsoft.com/cppblog/clear-functional-c-documentation-with-sphinx-breathe-doxygen-cmake/)
- [Adding doxygen support to CMakeLists.txt](http://www.miscdebris.net/blog/2019/02/25/adding-doxygen-support-to-cmakelists-txt/)
- [David/CMakeTemplate](https://github.com/DavidAce/CMakeTemplate)
- [Hunter](https://hunter.readthedocs.io/en/latest/index.html)
