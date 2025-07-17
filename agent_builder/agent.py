from typing import Any, List, Optional, Union

from openai import AsyncAzureOpenAI, AzureOpenAI
from openai._types import NOT_GIVEN, NotGiven
from openai.types.chat.chat_completion import ChatCompletion
from openai.types.chat.parsed_chat_completion import ParsedChatCompletion
from pydantic import BaseModel, Field

from agent_builder.prompt import Prompt


class AgentNode:
    def __init__(
        self,
        model: str,
        prompt: Prompt,
        user_prompt_injection: dict,
        temperature: float,
        output_format: Optional[Any] = None,
        system_prompt_injection: Optional[dict] = None,
    ):
        self.model = model
        self.prompt = prompt
        self.user_prompt_injection = user_prompt_injection
        self.system_prompt_injection = system_prompt_injection
        self.temperature = temperature
        self.output_format = NOT_GIVEN if output_format is None else output_format

    def get_system_message(self):
        if self.system_prompt_injection is None:
            return self.prompt.system_message
        return self.prompt.format_system_prompt(self.system_prompt_injection)

    def messages(self):
        return [
            {
                "role": "system",
                "content": self.get_system_message(),
            },
            {
                "role": "user",
                "content": self.prompt.format_user_prompt(self.user_prompt_injection),
            },
        ]

    def run(self):
        client = AzureOpenAI()
        if isinstance(self.output_format, NotGiven) or isinstance(self.output_format, dict):
            response = client.chat.completions.create(
                model=self.model,
                temperature=self.temperature,
                messages=self.messages(),
                response_format=self.output_format,
            )
        elif issubclass(self.output_format, BaseModel):
            response = client.beta.chat.completions.parse(
                model=self.model,
                temperature=self.temperature,
                messages=self.messages(),
                response_format=self.output_format,
            )
        else:
            raise ValueError(f"Invalid output_format, got {self.output_format}")
        return self.extract_response_content(response)

    async def arun(self):
        client = AsyncAzureOpenAI()
        if isinstance(self.output_format, NotGiven) or isinstance(self.output_format, dict):
            response = await client.chat.completions.create(
                model=self.model,
                temperature=self.temperature,
                messages=self.messages(),
                response_format=self.output_format,
            )
        elif issubclass(self.output_format, BaseModel):
            response = await client.beta.chat.completions.parse(
                model=self.model,
                temperature=self.temperature,
                messages=self.messages(),
                response_format=self.output_format,
            )
        else:
            raise ValueError(f"Invalid output_format, got {self.output_format}")
        return self.extract_response_content(response)

    def extract_response_content(self, response: Union[ParsedChatCompletion, ChatCompletion]) -> str:
        response_content = response.choices[0].message.content
        if response_content is None:
            raise ValueError(f"No response_content found: '{response_content}'")
        return response_content


class NameMapping(BaseModel):
    original_name: str = Field(description="The original name of the speaker in the transcription.")
    corrected_name: str = Field(
        description="The correct name of the speaker in the transcription, as determined based on the context of the transcription text. If the name could not be determined, the original name is used."
    )


class NameMapOutput(BaseModel):
    names: List[NameMapping] = Field(
        description="A list of objects which help to map original names to corrected names."
    )


def summarization_agent(summarization_prompt: Prompt, input_text: str) -> AgentNode:
    summarization_agent = AgentNode("gpt-4o", summarization_prompt, {"text": input_text}, 0.0, NameMapOutput)
    return summarization_agent