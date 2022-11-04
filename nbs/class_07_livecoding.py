# This is a piece of code that Ross recommends to have for later reference

import argparse
import pandas as pd

def arg_inputs():
    # initialise parser
    my_parser = argparse.ArgumentParser(description = "A script that says hello.")

    # add arguments
    my_parser.add_argument("-n", # incl. 4 pieces of information: - short name,
                        "--name", # -- long name,
                        type = str, # data type
                        required = True,
                        help = "the name to say hello") # and some help info
    my_parser.add_argument("-a",
                        "--age", 
                        type = int,
                        required = True,
                        help = "The age of the person") 

    # the list of arguments given
    args = my_parser.parse_args() # a list that contains all the arguments given from the command line.and

    # return list of arguments
    return args

# define function
def hello(name:str) -> str:
    print(f"Hello, my name is {name}! Here's my info:")

def person_info(name:str, age:int) -> pd.DataFrame:
    df = pd.DataFrame([[name, age]], columns=["name", "age"])
    print(df)

def main():
    #get the command line arguments
    arguments = arg_inputs()
    # run the hello function
    hello(arguments.name)
    person_info(arguments.name, arguments.age)

# the point of this is that this file contains pieces of code that can be both imported to other files, but can also be run from the command line. Here, we are just defining that if this piece of code is run from the command line, what we want to do is run the main() function. If it's imported from a notebook, it'll try to run the entire script, unless we add this piece of code. Then, it'll be able to just import the functions.
if __name__ == "__main__":
    main()