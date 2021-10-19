# codetest-art-institute-chicago

## Introduction
The purpose of this repository is to satisfy the requirements of StyleSage Data Operations code test for an interview.

## Configuration
Fork and/or clone this repo into your computer:

`git clone https://github.com/mariobru/codetest-art-institute-chicago.git` 

Give execution permissions to logparser.py if needed:

`sudo chmod 755 main.py`

You need to have installed in your environment the following Python 3.6 libraries:
* requests
* json
* csv
* random
* argparse

## How to use it
This scrip is very easy to use. You just need to run the following command:

`./main.py [-p] [-l]` 

```
optional arguments:
  -h, --help            show this help message and exit
  -p PAGE, --page PAGE  Enter the page number from 1 to 100 that the API
                        request will use. Default : 2
  -l LIMIT, --limit LIMIT
                        Set how many record each page should return. Default : 12
```



