#!/usr/bin/python3.9


if __name__== "__main__":
 import yaml
 with open("example1.yml") as f:
    result = yaml.load(f)
    print(result)
    type(result)