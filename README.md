
# Python-layer

The python-layer is a script inspired from [python-lambda](https://github.com/nficano/python-lambda) that can help managing aws layers. There are 5 available commands with options.

## Requirements
* Python 3
* GNU Linux

## Installation
You can create a new virtual environment on your computer and then install python-layer via pypi.
```pip install python-layer ```
## Getting Started


The script searches in a directory for the ```requirements.txt``` file and creates a zip with all the dependencies. If there are ```.py``` files, they are included in the zip.

To create a new layer:
``` layer build  path/to/mydir```

Here we suppose that ```mydir``` has at least the requirements file.

To deploy the layer to aws:
``` layer deploy -d myshortdescription --runtime python3.7 ```

To list the available layers:
```layer list ```

To set a layer to a lambda function (latest version of the layer):
``` layer set mylayer mylambda```

To download a layer
``` layer download mylayer```

## Notes
* Currently the script uses the credentials from the ```~/.aws/config``` file.