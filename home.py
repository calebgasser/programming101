import streamlit as st

st.title("Home")

st.markdown("""
## Projects

This is just a list of simple projects to get you familiar with common programming tasks. Feel free to take them on
in order or switch it up.

### 📝 Read 'n Write

Write a Python program that pulls in some data, parses and filters it, then outputs it to a file.
1. Use [www.dummyjson.com](www.dummyjson.com) to pull some fake 'post' data. [Here is the link to the documentation](https://dummyjson.com/docs/posts). Note, the examples are written in Javascript but the URL's that are being used will work in any language.
2. Convert the raw json string returned to a Python dictionary.
3. Examine the structure of the data you got back. You'll notice each 'post' has a list of 'tags'.
4. Choose a tag, then discard all posts without that tag.
5. Write the posts data, after you've filtered it, to a file called `filtered_posts.json`. It needs to be valid json format.
6. Check the structure of your JSON file using [www.jsonlint.com](https://jsonlint.com/). Do this step manually, not programmatically.
7. After you've verified the structure is correct, read the file back in and display the data to the console.
8. Run the program one last time, start to finish, and check the printed output. 

#### Concepts you'll need to understand

These are things you'll need to understand to complete this project.
""")

st.markdown("""
##### - Reading and writing files in Python.
[Read the documentation here](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files)
""")

st.markdown("""
##### - JSON
JSON, which stands for JavaScript Object Notation, is a way to store and exchange data. It's like a set of rules for formatting data so that it's easy for both humans and computers to understand. JSON is commonly used in web applications to send data from a server to a web page.

Imagine you have a bunch of information, like names and ages of people, and you want to store it in a way that's organized and easy to read. In JSON, this information is formatted in a specific way, using things like curly braces `{}` to group data, and square brackets `[]` for lists. Each piece of information is written in a key-value pair, like `"name": "Alice"`, where `"name"` is the key and `"Alice"` is the value.

Here's a simple example of JSON data:

```json
{
  "name": "Alice",
  "age": 30,
  "isStudent": false
}
```

This format is very popular because it's straightforward, easy to read, and can be quickly processed by computers. It's widely used on the internet for transferring data between a server and a web client.
""")

st.markdown("""
##### - Making requests to API(Application Programming Interface) end points
API endpoints are like specific addresses in a larger communication system used by software to talk to each other. Think of it as the way you access different services or information on the internet.

Let's use a real-world analogy: imagine you're in a big library. This library has many different sections (like science, history, fiction), and within each section, there are lots of books. If the library is the internet, then each book or section is like an API endpoint - a specific location where you can get certain information or services.

When a program wants to interact with another program or service (like getting weather data, posting a message on social media, or checking a bank account balance), it sends a request to the appropriate API endpoint. The endpoint is just a URL (an address on the internet) that specifies where to send these requests.

For example, if you have an app that shows weather forecasts, the app might send a request to a weather service's API endpoint to get the latest weather data. The endpoint processes this request and sends back the information the app asked for, like temperature, wind speed, etc.

In summary, API endpoints are specific points of interaction where applications can request and exchange data and services over the internet.

Here is an example in python:
""")
with st.echo():
    import urllib.request, json
    target_url = "https://dummyjson.com/users"
    with urllib.request.urlopen(target_url) as response:
        data = json.load(response)
st.write("**Contents of `data` returned from making a request**")
st.json(data, expanded=False)
