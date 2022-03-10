<h1 align ="center">
<img src="https://assets.website-files.com/6105315644a26f77912a1ada/610540e8b4cd6969794fe673_Holberton_School_logo-04-04.svg" height="50%" width="40%">
</h1>

# 💾 0x0E. SQL - More queries ✏️

### 🖋️ Concepts
>For this project, students are expected to look at these concepts:

*   Databases


<h1 align ="center">
<img src="https://www.tec-innova.mx/wp-content/uploads/2021/12/Imagen1.png" height="50%" width="40%">
</h1>

## 😊 Background Context
> Welcome to the AirBnB clone project!
***

### 🖋️ Description
First step: This is a SQL project and integration…
***

### 📋 General
* How to create a new MySQL user
* How to manage privileges for a user to a database or table
* What’s a PRIMARY KEY
* What’s a FOREIGN KEY
* How to use NOT NULL and UNIQUE constraints
* How to retrieve datas from multiple tables in one request
* What are subqueries
* What are JOIN and UNION

### 📂 files
***

## Installation
* Install MySQL 8.0 on Ubuntu 20.04 LTS: 
```
$ sudo apt update
$ sudo apt install mysql-server
...
$ mysql --version
mysql  Ver 8.0.25-0ubuntu0.20.04.1 for Linux on x86_64 ((Ubuntu))
$
```

*   Connect to your MySQL server:
```
$ sudo mysql
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 11
Server version: 8.0.25-0ubuntu0.20.04.1 (Ubuntu)

Copyright (c) 2000, 2021, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql>
mysql> quit
Bye
$
```
* Use “container-on-demand” to run MySQL

    *   Ask for container Ubuntu 20.04
    *   Connect via SSH
    *   OR connect via the Web terminal
    *   In the container, you should start MySQL before playing with it:
```
$ service mysql start                                                   
 * Starting MySQL database server mysqld 
$
$ cat 0-list_databases.sql | mysql -uroot -p                               
Database                                                                                   
information_schema                                                                         
mysql                                                                                      
performance_schema                                                                         
sys                      
$
```

## ✒️ Author
- **Pether Tejada** - _0x00. AirBnB clone - The console_ -
[<img src="https://img.shields.io/badge/GitHub-mainPage-blue">](https://github.com/Pether20)
