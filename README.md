# gtest-tools
Copyright (c) 2015-2018 FJTC. All rights reserved.

## Introduction

gtest-tools is a set of portable Python scripts that can help the creation of 
unit-tests for C/C++ using Google's googletest framework (https://code.google.com/p/googletest).

## History

* 2018.02.02: New scripts to launch gtestgengui for Windows and Linux;

## What is inside

### gtestgen

This is a small GUI tool that can be used to generate source code (header/source)
for Google Test unit tests. Those source codes are generated based on template files.

To run it, execute /path/to/gtestgen/gtestgengui.sh or c:\path\to\gtestgen\gtestgengui.bat
inside the directory that will hold the unit test files.

### sample-tools

Command line tools that can convert binary/hex strings into C/C++ constants.

## How to install

Download the repository from https://github.com/fjtc/gtest-tools and copy its
the files inside your project. Do not forget to edit the templates inside 
gtestgen/src (*.tpl) in order to ajust them to your needs.

## License

This software is released under the terms of "Modified BSD License". See LICENSE for the complete license.

