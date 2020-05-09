# Cpp-Project-Template

A C++ project template uses CMake with Doxygen, Sphinx integrated

## Used for

Two main things when starting a new Cpp project

- Dependency
- Documentation

And of course, a general purpose Cpp project structure

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

## Installation

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
- set up environment for documentation

  **Suggestion**: create a virtural python environment using [conda](https://docs.conda.io/en/latest/)

  - install required python packages

  ```bash
  > cd docs
  > pip install -r requirements.txt
  ```

  - change relavent content within `conf.py` and `index.rst`
    - `project` = 'cpp-project-template'
    - `copyright` = '2020, WilliamCodeBox'
    - `author` = 'WilliamCodeBox'
    - `release` = '1.0.0'
    - `sourceDir` = "../include"
    - `docOutputDir` = "./api"
    - `rootFileTitle` = "Library API"
  - Generate the docs

  ```bash
  > make html
  ```

## Configuration

### Documentation Customization

[CMake Doxygen Config](https://cmake.org/cmake/help/latest/module/FindDoxygen.html)

## References and Thanks to

- [Clear, Functional C++ Documentation with Sphinx + Breathe + Doxygen + CMake](https://devblogs.microsoft.com/cppblog/clear-functional-c-documentation-with-sphinx-breathe-doxygen-cmake/)
- [Adding doxygen support to CMakeLists.txt](http://www.miscdebris.net/blog/2019/02/25/adding-doxygen-support-to-cmakelists-txt/)
- [David/CMakeTemplate](https://github.com/DavidAce/CMakeTemplate)
- [Hunter](https://hunter.readthedocs.io/en/latest/index.html)
