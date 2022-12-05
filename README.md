# Desenvolvimento de aplicação para tratamento de dados - PUC

## Development

### Command line and environment

PYTHONPATH

```sh
export PYTHONPATH="\${PYTHONPATH}:/home/anderson.bolivar/Documentos/boli/puc-projeto"
```

```sh
sudo apt install python3.8-venv
python3 -m venv .venv
source .venv/bin/activate
which python3
```

Installing python modules:

```sh
python3 -m pip install -r requirements.txt
```

Running the project:

```sh
python -m index
```

Launch MySQL Workbench:

```sh
mysql-workbench
```

Python version:

```sh
python --version
Python 3.8.10
```

Invoking the Interpreter

### Tools

#### Integrated development environment - IDE: VS Code

[Visual Studio Code](https://code.visualstudio.com/)

Support for debugging, syntax highlighting, intelligent code completion, snippets, code refactoring and embedded Git;

#### High-level programming language: Python

[Dowload Python](https://www.python.org/downloads/)

Python is an interpreted, object-oriented, high-level programming language with dynamic semantics;

Its high-level built in data structures, combined with dynamic typing and dynamic binding, make it very attractive for Rapid Application Development, as well as for use as a scripting or glue language to connect existing components together;

Python's simple, easy to learn syntax emphasizes readability and therefore reduces the cost of program maintenance;

Python supports modules and packages, which encourages program modularity and code reuse;

The Python interpreter and the extensive standard library are available in source or binary form without charge for all major platforms, and can be freely distributed;

Python is simple to use, but it is a real programming language, offering much more structure and support for large programs than shell scripts or batch files can offer. On the other hand, Python also offers much more error checking than C, and, being a very-high-level language, it has high-level data types built in, such as flexible arrays and dictionaries;

Python allows you to split your program into modules that can be reused in other Python programs. It comes with a large collection of standard modules that you can use as the basis of your programs;

Python is an interpreted language, which can save you considerable time during program development because no compilation and linking is necessary;

The interpreter can be used interactively, which makes it easy to experiment with features of the language, to write throw-away programs, or to test functions during bottom-up program development. It is also a handy desk calculator;

Python enables programs to be written compactly and readably. Programs written in Python are typically much shorter than equivalent C, C++, or Java programs, for several reasons:

- the high-level data types allow you to express complex operations in a single statement;
- statement grouping is done by indentation instead of beginning and ending brackets;
- no variable or argument declarations are necessary.

Python is extensible: if you know how to program in C it is easy to add a new built-in function or module to the interpreter;

```sh

```

##### CLI

```sh
python [-bBdEhiIOqsSuvVWx?] [-c command | -m module-name | script | - ] [args]
```

Interactive Mode:

When called with standard input connected to a tty device, it prompts for commands and executes them until an EOF (an end-of-file character, you can produce that with Ctrl-D on UNIX or Ctrl-Z, Enter on Windows) is read;

```sh
python
```

When called with a file name argument or with a file as standard input, it reads and executes a script from that file.

```sh
python filename.py
```

When called with a directory name argument, it reads and executes an appropriately named script from that directory;

When called with -c command, it executes the Python statement(s) given as command;

When called with -m module-name, the given module is located on the Python module path and executed as a script;

```sh
python -m filename.py
```

##### Environment Variables

Environment variables are variables you store outside of your program that can affect how it runs;

PYTHONPATH

An environment variable that lets you add additional directories where Python looks for packages and modules;
It is used by user-defined modules to set the path so that they can be directly imported into a Python program;
It also handles the default search path for modules in Python;
PYTHONPATH variable includes various directories as a string to be added to the sys.path directory list;

```sh
export PYTHONPATH="\${PYTHONPATH}:/home/anderson.bolivar/Documentos/boli/puc-projeto"
```

##### Virtual Environment

Semi-isolated Python environment that allows packages to be installed for use by a particular application, rather than being installed system wide;
A virtual environment is a directory tree which contains Python executable files and other files which indicate that it is a virtual environment;
venv is the standard tool for creating virtual environments;

```sh
sudo apt install python3.8-venv
python3 -m venv .venv && source .venv/bin/activate
which python3
```

##### Installing Python Modules

pip is the preferred installer program;

```sh
python3 -m pip install -r requirements.txt
```

##### Executing modules as scripts

A module is a file containing Python definitions and statements;
The file name is the module name with the suffix .py appended;
Within a module, the module’s name (as a string) is available as the value of the global variable **name**;

```sh
python index.py
```

##### Packages

Packages are a way of structuring Python’s module namespace by using “dotted module names”. For example, the module name A.B designates a submodule named B in a package named A;
When importing the package, Python searches through the directories on sys.path looking for the package subdirectory;
The **init**.py files are required to make Python treat directories containing the file as packages;

#### MySQL

MySQL, the most popular Open Source SQL database management system, is developed, distributed, and supported by Oracle Corporation;
MySQL is a database management system. A database is a structured collection of data;
To add, access, and process data stored in a computer database, you need a database management system such as MySQL Server;
MySQL databases are relational;
A relational database stores data in separate tables rather than putting all the data in one big storeroom;
The SQL part of “MySQL” stands for “Structured Query Language”. SQL is the most common standardized language used to access databases;
MySQL software is Open Source. Open Source means that it is possible for anyone to use and modify the software;
The MySQL Database Server is very fast, reliable, scalable, and easy to use;
The MySQL Community Server provides a database management system with querying and connectivity capabilities, as well as the ability to have excellent data structure and integration with many different platforms;
The MySQL APT repository provides a simple and convenient way to install and update MySQL products with the latest software packages using Apt;
MySQL Workbench delivers visual tools for creating, executing, and optimizing SQL queries;

[MySQL Community Downloads](https://dev.mysql.com/downloads/)

MySQL Community Server[https://phoenixnap.com/kb/install-mysql-ubuntu-20-04]

MySQL APT Repository

MySQL Workbench[https://phoenixnap.com/kb/mysql-workbench-ubuntu]

```sh
sudo dpkg -i package.deb
sudo apt-get update
```

Check if MySQL Service Is Running:

```sh
mysql --version
sudo systemctl status mysql
```

Securing MySQL:

```sh
sudo mysql_secure_installation
```

Log in to MySQL Server:

```sh
mysql -u root -p
```

Launch MySQL Workbench:

```sh
mysql-workbench
```

## Concepts

### Compiled languages

Compiled languages are converted directly into machine code that the processor (CPU) can execute;
The target machine directly translates the program;
As a result, they tend to be faster and more efficient to execute than interpreted languages;
They also give the developer more control over hardware aspects, like memory management and CPU usage;
Compiled languages need a “build” step – they need to be manually compiled first.
You need to “rebuild” the program every time you need to make a change;
Compilation errors prevent the code from compiling;
Examples of pure compiled languages are C, C++, Erlang, Haskell, Rust, and Go;

### Interpreted languages

An interpreted language is a programming language where the instructions are not directly executed by the target machine, but instead, read and executed by some other program (virtual machine);
The source code is not directly translated by the target machine. Instead, a different program, aka the interpreter, reads and executes the code.
Interpreters run through a program line by line and execute each command;
Interpreted languages were once significantly slower than compiled languages;
There is only one step to get from source code to execution;
Interpreted programs can be modified while the program is running;
All the debugging occurs at run-time;
Examples of common interpreted languages are PHP, Ruby, Python, and JavaScript;

### Object-oriented programming (OOP)

Object-oriented programming (OOP) is a computer programming model that organizes software design around data, or objects, rather than functions and logic;
An object can be defined as a data field that has unique attributes and behavior;
OOP focuses on the objects that developers want to manipulate rather than the logic required to manipulate them;
This approach to programming is well-suited for programs that are large, complex and actively updated or maintained;
The first step in OOP is to collect all of the objects a programmer wants to manipulate and identify how they relate to each other -- an exercise known as data modeling.

Structure :
Classes are user-defined data types that act as the blueprint for individual objects, attributes and methods;
Objects are instances of a class created with specifically defined data;
Methods are functions that are defined inside a class that describe the behaviors of an object;
Attributes are defined in the class template and represent the state of an object. Objects will have data stored in the attributes field. Class attributes belong to the class itself;

Principles:
Encapsulation:
This principle states that all important information is contained inside an object and only select information is exposed;
Abstraction:
Objects only reveal internal mechanisms that are relevant for the use of other objects, hiding any unnecessary implementation code;
Inheritance:
Classes can reuse code from other classes. Relationships and subclasses between objects can be assigned, enabling developers to reuse common logic while still maintaining a unique hierarchy;
Polymorphism:
Objects are designed to share behaviors and they can take on more than one form;

Benefits:
Modularity:
Encapsulation enables objects to be self-contained, making troubleshooting and collaborative development easier;
Reusability:
Code can be reused through inheritance, meaning a team does not have to write the same code multiple times;
Productivity:
Programmers can construct new programs quicker through the use of multiple libraries and reusable code;
Easily upgradable and scalable:
Programmers can implement system functionalities independently.
Security:
Using encapsulation and abstraction, complex code is hidden, software maintenance is easier and internet protocols are protected.
Flexibility:
Polymorphism enables a single function to adapt to the class it is placed in. Different objects can also pass through the same interface.

### Dynamic typing

Perform type checking at runtime;
Can compile even if they contain errors;
Do not require declare the data types variables before assigned values;

### Static typing

Perform type checking at compile time;
Fail to compile until the errors have been fixed;
Require declare the data types of variables before assigned values;

### MySQL

SELECT: indica quais colunas que serão apresentadas como resultado da consulta.

FROM: identifica as tabelas de onde serão trazidos os dados da consulta.

WHERE: apresenta as restrições ou filtros que serão aplicadas aos dados.

ORDER BY: classifica as linhas retornadas pela consulta.

FUNÇÕES AGREGADAS
Função Descrição
AVG(coluna) calcula a média de todos os valores para aquela coluna
COUNT(coluna) conta o número de valores não nulos para coluna
COUNT(\*) conta o número de linhas na tabela
MAX(coluna) retorna o valor máximo para coluna
MIN(coluna) retorna o valor mínimo para coluna
SUM(coluna) calcula a soma dos valores para coluna
