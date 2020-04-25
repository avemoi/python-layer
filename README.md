
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
``` layer deploy path/to/zip -d myshortdescription --runtime python3.7 ```

To deploy the layer to aws to a specific region
 ```layer deploy path/to/zip -r region_name```

To deploy the layer to aws to a specific region and to a specific profile (e.g. dev profile) 
```layer deploy path/to/zip -p dev_profile -r region_name``` 

To list the available layers:
```layer list ```

To list the available layers from a specific region:
```layer list -r region_name```

To list the available layers from a specific region and from a specific profile (e.g. dev profile):
```layer list -r region_name -p dev_profile```

To set a layer to a lambda function (appends the latest version of the layer):
``` layer set mylayer mylambda```

To set a layer to a lambda function (appends the latest version of the layer) to a specific region:
``` layer set mylayer mylambda -r region_name```

To set a layer to a lambda function (appends the latest version of the layer) to a specific region and to a specific profile:
``` layer set mylayer mylambda -p dev_profile -r region_name```

To set a list of layers:
``` layer set mylayer1,mylayer2 mylambda```

To set a list of layers replacing the older ones :
``` layer set mylayer1,mylayer2 mylambda -d```

To download a layer
``` layer download mylayer```

To download a layer from a specific region:
``` layer download mylayer -v version_number -r region_name```

To download a layer from a specific region and from a specific profile (e.g. dev profile):
``` layer download mylayer -v version_number -r region_name -p dev_profile```

## Notes
* Currently the script uses the credentials from the ```~/.aws/config``` file.