
# HashCash module for Python 3

## Prerequsites
`Java 8`

## Setup
`./gradlew clean build`

## Usage
### From REPL/scripts
```
import com.prussell.hashcash.HashCash;

HashCash.generate(15, "some_resource_string");
HashCash.isValid("a_hashcash_stamp");
```
