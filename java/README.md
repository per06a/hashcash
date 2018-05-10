
# HashCash library for Java

## Prerequsites
`Java 8`

## Setup
`./gradlew clean build`

## Usage
### From Java files
```
import com.prussell.hashcash.HashCash;

HashCash.generate(15, "some_resource_string");
HashCash.isValid("a_hashcash_stamp");
```
