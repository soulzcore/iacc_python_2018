# Virtual Environments

> Python today has multiple different versions used in production and lots of different libraries

> Based on the application and user preference a certain combination of python and library versions might be needed which might not work for a different application

> In python a Virtual Environment can be created which is isolated and functions as its own ecosystem of packages

> Multiple Virtual Environments can be created on the same machine

> Each Virtual Environment will isolated from the others and will not cause any conflicts

> In essence a virtual environment is a directory where the required python version and packages are copied.  


**Installation**
```python

pip install virtualenv

```

**Creating Virtual Environments**
> Create a new folder where you want the virtual environment to live

**From the Shell**

> cd into the new directory

> Run the following command

```Shell

python3 -m venv environment1

```

> environment1 is the name of the new environment

> you can create multiple environments using the same syntax, just make sure you create a new folder for every new environment

> After the environment is created, the following directories and files will be created in the environment folder

```python

├── bin
│   ├── activate
│   ├── activate.csh
│   ├── activate.fish
│   ├── easy_install
│   ├── easy_install-3.7
│   ├── pip
│   ├── pip3
│   ├── pip3.7
│   ├── python
│   ├── python3
│   └── python3.7 
├── include
├── lib
│   └── python3.7
│       └── site-packages
└── pyvenv.cfg

```

**Activating a Virtual Environment**

> To use a virtual environment that was already created, it will have to be activated

**Windows Activation**

> Cd into the virtual environment in the command prompt  and execute the activate.bat file

```shell
cd environment1

Scripts\activate.bat

```


**Mac/Unix**
> Cd into the virtual environment in the command prompt  and execute the activate file



```shell
cd environment1
source bin/activate

```

> After an Environment is activated, any package versions can be installed using pip without having to worry about conflicts with other versions

**Deactivating**

> To deactivate a virtual environment simply type deactivate in the windows command prompt or mac shell
