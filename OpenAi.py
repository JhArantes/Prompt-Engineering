
from openai import OpenAI
client = OpenAI()

response = client.responses.create(
    model="gpt-4.1",
    input="Write a one-sentence bedtime story about a unicorn."
)

print(response.output_text)

#=====================================================

from openai import OpenAI
client = OpenAI()

response = client.responses.create(
    model="gpt-4.1",
    input=[
        {
            "role": "developer",
            "content": "Talk like a pirate."
        },
        {
            "role": "user",
            "content": "Are semicolons optional in JavaScript?"
        }
    ]
)

print(response.output_text)


# Prompt Example
prompt = '''

# Identity

You are coding assistant that helps enforce the use of snake case 
variables in JavaScript code, and writing code that will run in 
Internet Explorer version 6.

# Instructions

* When defining variables, use snake case names (e.g. my_variable) 
  instead of camel case names (e.g. myVariable).
* To support old browsers, declare variables using the older 
  "var" keyword.
* Do not give responses with Markdown formatting, just return 
  the code as requested.

# Examples

<user_query>
How do I declare a string variable for a first name?
</user_query>

<assistant_response>
var first_name = "Anna";
</assistant_response>
'''

client = OpenAI()

response = client.responses.create(
    model="gpt-4.1",
    input=[
        {
            "role": "user",
            "content": prompt
        },
        {
            "role": "user",
            "content": "How do I declare a string variable for a first name?"
        }
    ]
)

print(response.output_text)










