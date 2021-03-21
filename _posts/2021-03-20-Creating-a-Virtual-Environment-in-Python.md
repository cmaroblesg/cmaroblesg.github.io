---
layout: post
---
Python applications needs lot of package and libraries that most of the time are not included when installed from scratch. Sometimes, it is needed to include specific version library to work with, and most of the time the newest libraries come with bugs or doesn't have full integration with the new environment.

So, the most common solution is to create a virtual environment, that contains the libraries needed for a particular project. It means that, with a virtual environment you will be able to create a self-contained directory tree containing a particular Python version.

### Creating a Python *Virtual Environment*
This isn't a difficult task and you need only to select a folder or directory that will contains the virtual environment.

```
python -m venv <folder_path>/.
```
