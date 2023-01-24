# Desenvolvimento de aplicação para tratamento de dados

Projeto do primeiro semestre do curso Banco de Dados da PUC Minas Virtual.

## Etapas

### 1ª Etapa: Grupos e Bases de Dados

Definição dos grupos.
Definição das bases de dados.


### 2ª Etapa: Arquitetura e Metodologia

Definição da arquitetura e da metodologia para o tratamento dos dados.

### 3ª Etapa: Captura dos dados

Desenvolvimento da solução para tratamento inicial de dados (acesso, seleção e carga dos dados).

### 4ª Etapa: Limpeza e Transformação

Implementação da solução para limpeza e transformação dos dados.

### 5ª Etapa: Visualização de Dados

Implementação da apresentação visual dos dados;

### 6ª Etapa: Apresentação Final do Projeto

Elaboração da apresentação final do projeto.

## Setup and running the project

### Linux

#### PYTHONPATH

The PYTHONPATH variable holds a string with the name of various directories that need to be added to the sys.path directory list by Python. It is used to set the path for the user-defined modules so that it can be directly imported into a Python program. It is also responsible for handling the default search path for Python Modules.  

```sh
export PYTHONPATH="\${PYTHONPATH}:/home/anderson.bolivar/Documentos/boli/puc-projeto"
```

#### Virtual Enviroment

A virtual environment is a tool that helps to keep dependencies required by different projects separate by creating isolated python virtual environments for them. 

```sh
sudo apt install python3.8-venv
python3 -m venv .venv
source .venv/bin/activate
which python3
```

#### Python modules

```sh
python3 -m pip install -r requirements.txt
```

#### Running the project

```sh
python -m index
```

### Windows

#### Virtual Enviroment

```sh
py -m venv .venv
.venv/bin/activate
```

#### Python modules

```sh
py -m pip install -r requirements.txt
```

#### Running the project

```sh
python -m index
```



## Tools

### Integrated development environment - IDE: VS Code

[Visual Studio Code](https://code.visualstudio.com/)

Support for debugging, syntax highlighting, intelligent code completion, snippets, code refactoring and embedded Git;

### High-level programming language: Python

[Dowload Python](https://www.python.org/downloads/)

Python is an interpreted, object-oriented, high-level programming language with dynamic semantics;

### Database: MySQL

MySQL, the most popular Open Source SQL database management system, is developed, distributed, and supported by Oracle Corporation;



