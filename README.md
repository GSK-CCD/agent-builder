# Agent Builder

Agent builder is a library which helps to quickly create simple agents in AI applications.

## Agents

### Creating an Agent Node

To create an Agent Node, you'll need to instantiate the `AgentNode` class and pass in the required parameters:

```python
agent_node = AgentNode(
    model="gpt-4o",  # The OpenAI model to use
    prompt=Prompt(system_message="System message", user_message_template="User message template"),
    user_prompt_injection={"text": "User input text"},
    temperature=0.0,  # The temperature parameter for the model
    output_format=NameMapOutput  # The output format for the response (a Pydantic model)
)
```

### Running the Agent Node

Once you've created an Agent Node, you can run it using the `run` method:

```python
response = agent_node.run()
```

This will send a request to the OpenAI API and return the response.

### Running the Agent Node Asynchronously

If you want to run the Agent Node asynchronously, you can use the `arun` method:

```python
async def main():
    response = await agent_node.arun()
    print(response)

asyncio.run(main())
```

## Prompts

The `Prompt` class is designed to help you create and format prompts for your AI models. Here's a step-by-step guide on how to use it:

### Creating a Prompt Object

To create a `Prompt` object, you need to provide two string arguments: `system_message` and `user_message_template`. These represent the system message and the user message template, respectively.

```python
prompt = Prompt(system_message="Hello, how can I assist you?", user_message_template="User: {user_input}")
```

### Formatting Prompts

You can format the prompts using the `format_user_prompt` and `format_system_prompt` methods. These methods take a `string_injection_mapping` dictionary as an argument, which maps variable names to their corresponding values.

```python
string_injection_mapping = {"user_input": "I need help with my project"}
formatted_user_prompt = prompt.format_user_prompt(string_injection_mapping)
print(formatted_user_prompt)  # Output: User: I need help with my project
```

## Embeddings

The package also contains a helper function which lets you see how many tokens a given string would use in a given model.