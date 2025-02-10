#!/usr/bin/env python3

import ipdb

def tracing_the_function():
    """
    This function demonstrates the use of ipdb for debugging.
    It sets a breakpoint and prints a variable after the breakpoint.
    """
    inside_the_function = "We're inside the function"
    print(inside_the_function)
    this_variable_hasnt_been_interpreted_yet = "The program froze before it could read me!"
    print("We're about to stop because of ipdb!")
    ipdb.set_trace()
    print(this_variable_hasnt_been_interpreted_yet)


tracing_the_function()