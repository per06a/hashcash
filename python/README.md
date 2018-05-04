
# HashCash module for Python 3

## Prerequsites
`python3 >= 3.5`

This module uses modern Python type hints and so requires a modern
Python. Any version >= 3.5 works.

## Setup
`pip install hashcash/python`

## Usage
### From REPL/scripts
```
import hashcash

stamp = hashcash.generate(15, "some resource string to hash")
hashcash.validate(15, stamp)
```

### From the command line
```
# Generate
python hashcash.py NBITS RESOURCE_STRING

# Validate
python hashcash.py -v NBITS STAMP
```