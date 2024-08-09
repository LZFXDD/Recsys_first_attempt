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
                 agent_prompt: PromptTemplate = perceive_agent_prompt,
                 preceive_llm: AnyOpenAILLM = AnyOpenAILLM(
                     temperature=0,
                     model_name='gpt-3.5-turbo',
                     model_kwargs={"stop": "\n"},
                     openai_api_key=os.environ['OPENAI_API_KEY']
                 )):
        self.llm = preceive_llm
        self.preceive_examples = PERCEIVE_EXAMPLES
        self.agent_prompt = agent_prompt
        self._is_found = False
    def perceive_agent_generate(self, title: str) -> str:
        if format_string(title) not in dataset.keys():
            return "The movie is not found in the dataset. Please try another."

        self._is_found = True
        self.title = format_string(title)
        return format_string(self.llm(self._build_agent_prompt()))

    def user_comment_analysis(self, comment) -> str:
        pass

    def _build_agent_prompt(self) -> str:
        return self.agent_prompt.format(
            examples=self.preceive_examples,
            title=self.title,
            year=dataset[self.title][0],
            genres=dataset[self.title][1],
        )

###字符串处理###
def format_string(string: str) -> str:
    return string.strip('\n').strip().replace('\n', '')