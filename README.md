# Custom Assembler and Simulator for CSE 112 Computer Organization

<br />

This project involves the development of a custom assembler and simulator. It is a collaborative effort with contributions from multiple contributors. Below is a detailed guide on the project, its structure, and information about each component.
This project was done within the course work of CSE 112 Computer Organisation under Prof. Tammam Tillo at IIIT Delhi.

## Table of Contents
1. [Introduction](#introduction)
2. [Code Structure](#code-structure)
3. [Contributors](#contributors)

## Introduction

The project focuses on building a custom assembly-like language compiler and simulator. The language includes various instructions, and the project is divided into different files, each serving a specific purpose.

## Code Structure

### Main.py
- Responsible for reading input, gathering files, and compiling the final assembler.
- Detects and handles errors related to variables and labels.
- Converts high-level instructions into machine code using the OPcode table.

### Simulator.py
- Simulates the compiled code execution.
- Manages registers, memory, and flags during the simulation.
- Provides functionality for arithmetic operations, comparisons, and control flow.

### Helper.py
- Contains essential helper functions used throughout the project.
- Implements functions for binary-to-decimal conversion, error handling, and basic operations.

### Error.py
- Defines error codes for different types of errors that may occur during compilation and simulation.
- Provides a standardized way to handle and report errors in the code.

### OPcode.py
- Includes the OPcode table, mapping mnemonics to binary codes and instruction types.
- Defines the binary representation and type for each supported instruction.

### Dic.py
- Contains dictionaries and constants used in the project.
- Provides a centralized location for storing and managing shared data.

### Functions.py
- Includes basic but important functions used consistently throughout the project.
- Implements functions for binary manipulation, conversions, and operations.

### run.sh
- A script that combines compilation and simulation for convenience.
- Executes the `Main.py` and `Simulator.py` scripts sequentially.

<br />

---

## Contributors

The project has been made possible by the contributions of the following individuals:

- Nakul Garg - [GitHub Profile](https://github.com/NakulGarg-IIITD)        : Helper.py
- Sankit - [GitHub Profile](https://github.com/Sankit2512)                 : Helper.py, Error.py, OPcode.py
- Sanyam Garg - [GitHub Profile](https://github.com/SanyamGarg12)          : Main.py
- Yash Bhardwaj - [GitHub Profile](https://github.com/regular-life)        : Functions.py


Feel free to reach out to the contributors for questions or issues related to their respective contributions.

If you encounter any issues or have suggestions for improvement, please provide feedback to help enhance the project.