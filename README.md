# Combination for presentations – JuDo = JUpyter +DrawiO

Powerpoint & Google Docs have the best user experience when it comes to building slides, 
**BUT** when having to deliver talks about one’s tech design/code/architecture, these tools falls short in the following situations 

| Situation      | Inefficient practices with PPT / Google Docs |
| ----------- | ----------- |
| Ingest existing code snippets or outputs into slide  content	| Copy+paste code with formatting from IDE or take screenshots |
| Show realistic developer experience with code snippets and their output to illustrate execution flow of APIs/SDKs/code | 	Take successive screenshots or take a screen recording of console output |
| Use rich diagramming tool with support for stencils/templates that support technical paradigms |	Export diagrams maintained in a fully featured diagramming tools into slide deck |
| Collaborating/brainstorming within inline whiteboards	|Whiteboarding canvas for real time collaboration during delivery of the talk has less features  & need to ported eventually into target state diagramming tool |

In summary, to develop technical slides, it requires the author to **context switch** between 3 softwares :-
1. Presentation software, 
2. Diagramming software 
3. IDE that show cases code flows


# Install

## Prerequisite 

1. Python 3.10: Obviously python,  and there is no better way to manage multiple python versions than using [pyenv](https://github.com/pyenv/pyenv).
To install python, and our specific version is now as easy as:-
```
pyenv install 3.10
```
2. Poetry: Python package manager to manage dependencies for your project. See install steps [here](https://python-poetry.org/docs/)

## Running Jupyter with drawing extensions
Run the following to install jupyter, ipydrawio and other dependencies as well as to run jupyterlab instance within the virtual env setup for your project :-

```bash
poetry install # create virtual env and pull dependencies
poetry run jupyter lab # run jupyterlab within this virtual env
```

# Distributing deck

Render the drawings in presentation mode. As a best practice setup a global var and run all the cells again :)
**TODO** Currently conversion to image from drawio has to be done manually by using the UI option. See backlog item around automatic generation of image(png) from drawio

```
poetry run jupyter nbconvert deck.ipynb --to slides
```


# Contributing

* Check the issues list
* To setup local virtualenv with dependencies managed in poetry toml file:-
```
poetry shell
code . # to start VSCode within the current folder
```