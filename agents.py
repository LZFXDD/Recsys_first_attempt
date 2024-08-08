import os

from langchain.docstore.base import Docstore
from langchain import Wikipedia
from langchain.agents.react.base import DocstoreExplorer
from langchain.prompts import PromptTemplate

from llm import AnyOpenAILLM
from fewshots import PERCEIVE_EXAMPLES
from prompts import perceive_agent_prompt
class PerceiveAgent:
    def __init__(self,
                 docstore: Docstore = Wikipedia(),
                 agent_prompt: PromptTemplate = perceive_agent_prompt,
                 preceive_llm: AnyOpenAILLM = AnyOpenAILLM(
                     temperature=0,
                     model_name='gpt-3.5-turbo',
                     model_kwargs={"stop": "\n"},
                     openai_api_key=os.environ['OPENAI_API_KEY']
                 )):
        self.docstore = DocstoreExplorer(docstore)
        self.llm = preceive_llm
        self.preceive_examples = PERCEIVE_EXAMPLES
        self.agent_prompt = agent_prompt

    def _build_agent_prompt(self) -> str:
        return self.agent_prompt.format(
            examples=self.preceive_examples,
            scratchpad=self.scratchpad,
        )

###字符串处理###
def format_string(string: str) -> str:
    return string.strip('\n').strip().replace('\n', '')