import streamlit as st

st.echo()
st.title("Quick Reference")
st.warning("Note: All calls to `st.` are for display purposes.")
st.markdown("## Data Types")

with st.echo():
    foo = 1 # Integer
    bar = 2.0 # Float
    baz = "Hello, world!" # String
    people = ["Dave", "John", "Smith"] # List
    people2 = {"name": "Dave", "age": 32} # Dictionary
    people3 = ("Sally", "Beth", "Jill") # Tuple

st.markdown("## Using Lists")

with st.echo():
    my_list = [] # Create a list
    my_other_list = [1, 2, 3] # Create a list with default values.
    single_item = my_other_list[0] # Get a single item from a list by index. (starts at 0)
    my_list.append("Joe") # Add an item to the end of the list
    length = len(my_list) # Get the length of a list
    some_item = my_list.pop() # Remove an item from the end of the list
    for item in my_other_list: # Iterate over the items in a list
        st.write(item)

st.markdown("## Using Dictionaries")

with st.echo():
    my_dict = {} # Create an empty dictionary.
    my_dict = {"name": "Dave", "age": 32} # Create a dictionary with inital values.
    my_dict["gender"] = "Male" # Add an item to a dictionary
    for key, value in my_dict.items(): # Iterate over a dictionary
        st.write(f"Key({key}): Value({value})")

st.markdown("## Functions")

with st.echo():
    def some_function(some, thing=10): # Creating a function with 2 parameters (arity of 2).
        """
        This is a function doc comment
        :param some: Explain what the parameter is
        :param thing: And the type of the parameter
        :return: Explain what you're returning from the function
        """
        return some + thing
    my_return_value = some_function(20) # Call the function and assign the return value to a variable.
    st.write(my_return_value)