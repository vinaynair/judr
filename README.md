# JuDr - JUpyter DRawing - Building technical presentations with inline drawing utilities

## Current stack for authoring slides
Powerpoint & Google Docs have the best user experience when it comes to building slides, 
**BUT** when having to deliver talks about one’s tech design/code/architecture, these tools falls short in the following situations 

| Situation      | Inefficient practices with PPT / Google Docs |
| ----------- | ----------- |
| Ingest existing code snippets or outputs into slide  content	| Copy+paste code with formatting from IDE or take screenshots |
| Show realistic developer experience with code snippets and their output to illustrate execution flow of APIs/SDKs/code | 	Take successive screenshots or take a screen recording of console output |
| Use rich diagramming tool with support for stencils/templates that support technical paradigms |	Export diagrams maintained in a fully featured diagramming tools into slide deck |
| Collaborating/brainstorming within inline whiteboards	|Whiteboarding canvas for real time collaboration during delivery of the talk has less features  & need to ported eventually into target state diagramming tool |

In summary, to develop technical slides, it requires the author to **context switch** between 3 types of softwares :-
1. Presentation software, eg Powerpoint, Google Docs 
2. Diagramming software, eg Drawio, Excalibur, Figma, 
3. IDE that show cases code flows,eg: VS Code, IntelliJ, Jupyter Lab



# Jupyter as IDE for developing slides

Jupyter lab provides a great IDE for rapidly iterating on code with text markup that allows for ideal setup for authoring slide content.
With ipydrawio plugin, one can author drawio diagrams inline with Jupyter lab as well. 

JuDr brings Jupyter with drawing utils such as 
* Drawio extension to author diagrams 
* Py utils to present draw editor as well as render image for exporting into various formats for distribution




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

Convert the python notebook into html
```
poetry run jupyter nbconvert deck.ipynb --to slides
```

Before that remember to render the drawings in presentation mode. 
As a best practice setup a global var and run all the cells again. 
From [deck.ipynb](/deck.ipynb)

```py

from slides.drawio import draw
OVERRIDES={'width':1200, 'height':800}
PRESENTATION=False
# render drawio 
draw('slide1.dio',overrides=OVERRIDES,presentation_mode=PRESENTATION)
```



**TODO** Currently conversion to image from drawio has to be done manually by using the UI option. See [backlog item]((https://github.com/vinaynair/judr/issues/1)) around automatic generation of image(png) from drawio



# Contributing

* Check the issues list
* To setup local virtualenv with dependencies managed in poetry toml file:-
```
poetry shell
code . # to start VSCode within the current folder
```


# FAQ

## Why not use diagram-as-code tools such as mermaidjs

Note that there is an argument to be made that one can use various "diagram as code" tools too such as mermaidjs and plantuml 
**BUT** generally such tools suffer from the following drawbacks when compared to Drawio :-
* need to learn a totally new language or sdk when drawing and editing especially is such a visual exercise with mouse. When diagrams get complex these diagram-as-code snippets become unmanageable
* diagramming markup languages are constrained to specific domains or archtetypes, for eg you can use it to make flowcharts but if you want to create BPMN diagrams you need to find another tooling for it.
* lack feature parity in general when it comes to how one can edit the diagram to be visually appealing
* systematic layout engines can**not** be as fluid as we want these diagrams to be when it comes to communicating the intent via manual visual placement of widgets

Where these tools generally shine when it comes to Drawio is that one can see the edits to diagrams in PRs(git diff) to review and to edit.
Again whether one wants to create diagrams for peer-reviewed via text or via visual examination (via summary in git commit message) is the choice one has to make :) 

Maybe a backlog item it to use a ML model to diff two images :) 