# Agent Builder

Agent builder is a library which helps to quickly create simple agents in AI applications. The library only works for OpenAI models deployed 
in Azure.

## Agents

### Creating an Agent Node

To create an Agent Node, you'll need to instantiate the `AgentNode` class and pass in the required parameters. There are two main ways to 
deploy an OpenAI model in Azure, each of which will require a different set of parameters.

#### Standard Subdomain

If you do not provide a custom subdomain for your Azure OpenAI Account resource, then your endpoint will contain the location of the 
resource deployment in the following format:

```python
https://MY_RESOURCE_LOCATION.api.cognitive.microsoft.com
```

With standard subdomains, the authentication is done via an API key. If you are using a standard subdomain, you will need to set the API key
to an environment variable which your application has access to. This environment variable also must be named `AZURE_OPENAI_API_KEY`, 
otherwise it will not be picked up properly by the client and will fail to authenticate.

Here is a basic example of how to create an Agent Node with a standard subdomain:

```python

agent_node = AgentNode(
    model="chatgpt4-dev",  # The name of the deplopyment of the OpenAI model in Azure. So if you deployed the o1 model with the deployment name chat01, then you would pass in chat01
    prompt=Prompt(system_message="System message", user_message_template="User message: {text}"),
    user_prompt_injection={"text": "User input text"},
    api_version="2023-03-15-preview",
    azure_endpoint="https://MY_RESOURCE_LOCATION.api.cognitive.microsoft.com",
    temperature=0.0,  # The temperature parameter for the model. Some models do not support this parameter and require it to be set to 1
)
```

#### Custom Subdomain

If you do provide a custom subdomain for your Azure OpenAI Account resource, then your endpoint will contain the name of the Azure OpenAI
resource in the following format:

```python
https://MY_AZURE_OPENAI_SERVICE.openai.azure.com
```

With custom subdomains, the authentication is done via a token provider. If you are using a custom subdomain, you will need to pass in a
token provider, which can be created using the `get_bearer_token_provider` function.

```python
# The AzureDeveloperCliCredential and ManagedIdentityCredential classes can be imported from either azure.identity or azure.identity.aio
# with the latter being the async variant. Running the agent as async is done using the .arun() method after you have created the agent node
azure_credential: Union[AzureDeveloperCliCredential, ManagedIdentityCredential]
if os.getenv("WEBSITES_PORT"):  # Some environment variable determining whether you are running locally or in Production
    azure_credential = ManagedIdentityCredential() # will get the token from the managed identity of the application running in prod
else:
    azure_credential = AzureDeveloperCliCredential(process_timeout=60) # will get the token from your `azd auth login` user
token_provider = get_bearer_token_provider(azure_credential, "https://cognitiveservices.azure.com/.default")
```

Here is a basic example of how to create an Agent Node with a custom subdomain:

```python
agent_node = AgentNode(
    model="chatgpt4-dev",  # The name of the deplopyment of the OpenAI model in Azure. So if you deployed the o1 model with the deployment name chat01, then you would pass in chat01
    prompt=Prompt(system_message="System message", user_message_template="User message: {text}"),
    user_prompt_injection={"text": "User input text"},
    api_version="2023-03-15-preview",
    azure_endpoint="https://MY_AZURE_OPENAI_SERVICE.openai.azure.com",
    token_provider=token_provider,
    temperature=0.0,  # The temperature parameter for the model. Some models do not support this parameter and require it to be set to 1
)
```

### Running the Agent Node

Once you've created an Agent Node, you can run it using the `run` method:

```python
response = agent_node.run()
```

Or if you want to use the Async client, using the `arun` method:

```python
async def main():
    response = await agent_node.arun()
    print(response)

asyncio.run(main())
```

This will send a request to the OpenAI API and return the response.

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