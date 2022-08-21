---
layout: post
toc: true
title: "Creating a Python Virtual Environment"
categories: [Coding]
tags: [Python]
author: César Robles
---
Python applications needs lot of package and libraries that most of the time are not included when installed from scratch. Sometimes, it is needed to include specific version library to work with, and most of the time the newest libraries come with bugs or doesn't have full integration with the new environment.

So, the most common solution is to create a virtual environment, that contains the libraries needed for a particular project. It means that, with a virtual environment you will be able to create a self-contained directory tree containing a particular Python version.

### Creating a Python *Virtual Environment*
This isn't a difficult task and you need only to select a folder or directory that will contains the virtual environment.

```
python3 -m venv <folder_path>/.
```
![Folder path](/imag/post_images/folder_path.png)

### Using the Virtual Environment
There are two different ways to activate the virtual environment and it depends on the Operating System:
* For Windows:
```
virtual_env_path\Scripts\activate.bat
```
* For Mac or Linux.
```
source virtual_env_path/bin/activate
```

When finish don't forget to *deactivate* your virtual environment. Just type 'deactivate' in both Operating Systems.
```
deactivate
```

### Managing package with *pip*

It is possible to install, upgrade, and remove packages using a program called **pip**.
For reference use [pypi.org](https://pypi.org) to verify the availability of the library. However, it is possible to search using pip:
```
pip search pandas
```

it's possible to install a package:
```
pip install pandas
```

Also, it is possible to specify the version of the library:
```
pip install requests==2.6.0
```

Another important feature is to upgrade the libraries:
```
pip install --upgrade pandas
```

To list the installedd libraries just type.
```
pip list
```

To retrieve information about a particular package:
```
pip show pandas
```

Create a list of installed libraries:
```
pip freeze > libraries_list.txt
```

To install all the libraries in  a new environment:
```
pip install -r libraries_list.txt
```

Consult the [Installing Python Modules](https://docs.python.org/3/installing/index.html#installing-index) guide for complete documentation for pip. When you’ve written a package and want to make it available on the Python Package Index, consult the [Distributing Python Modules](https://docs.python.org/3/distributing/index.html#distributing-index) guide.
