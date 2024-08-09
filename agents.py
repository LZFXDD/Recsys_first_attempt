import os

from langchain.docstore.base import Docstore
from langchain import Wikipedia
from langchain.agents.react.base import DocstoreExplorer
from langchain.prompts import PromptTemplate

from llm import AnyOpenAILLM
from fewshots import PERCEIVE_EXAMPLES
from prompts import perceive_agent_prompt
from dataset_preprocess import dataset

class PerceiveAgent:
    def __init__(self,
                 movidId: int,
                 agent_prompt: PromptTemplate = perceive_agent_prompt,
                 preceive_llm: AnyOpenAILLM = AnyOpenAILLM(
                     temperature=0,
                     model_name='gpt-3.5-turbo',
                     model_kwargs={"stop": "\n"},
                     openai_api_key=os.environ['OPENAI_API_KEY']
                 )):
        self.movidId = movidId
        self.llm = preceive_llm
        self.preceive_examples = PERCEIVE_EXAMPLES
        self.agent_prompt = agent_prompt
    def perceive_agent(self) -> str:

        return format_string(self.llm(self._build_agent_prompt()))

    def _build_agent_prompt(self) -> str:
        return self.agent_prompt.format(
            examples=self.preceive_examples,
            title=dataset[self.movidId][0],
            year=dataset[self.movidId][1],
            genres=dataset[self.movidId][2],
        )

###字符串处理###
def format_string(string: str) -> str:
    return string.strip('\n').strip().replace('\n', '')