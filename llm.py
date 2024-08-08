from typing import Union, Literal
from langchain.chat_models import ChatOpenAI
from langchain import OpenAI
from langchain.schema import (
    HumanMessage
)


class AnyOpenAILLM:
    """
    一个通用的OpenAI语言模型类，可以处理不同的模型类型，包括文本补全和聊天。
    """

    def __init__(self, *args, **kwargs):
        """
        类的构造函数，初始化AnyOpenAILLM实例。

        参数:
            *args: 可变参数，传递给OpenAI或ChatOpenAI构造函数的参数。
            **kwargs: 关键字参数，传递给OpenAI或ChatOpenAI构造函数的参数。
        """
        # 从关键字参数中获取模型名称
        model_name = kwargs.get('model_name', 'gpt-3.5-turbo')
        # 根据模型名称确定模型类型
        if model_name.split('-')[0] == 'text':
            # 如果模型名称以'text'开头，使用OpenAI进行文本补全
            self.model = OpenAI(*args, **kwargs)
            self.model_type = 'completion'  # 设置模型类型为'completion'
        else:
            # 否则，使用ChatOpenAI进行聊天
            self.model = ChatOpenAI(*args, **kwargs)
            self.model_type = 'chat'  # 设置模型类型为'chat'

    def __call__(self, prompt: str):
        """
        调用模型以生成响应。

        参数:
            prompt (str): 输入的提示字符串。

        返回值:
            str: 模型的响应字符串。
        """
        if self.model_type == 'completion':
            # 如果模型类型是'completion'，直接调用OpenAI的模型
            return self.model(prompt)
        else:
            # 如果模型类型是'chat'，构造聊天消息列表并调用ChatOpenAI的模型
            return self.model(
                [
                    HumanMessage(
                        content=prompt,
                    )
                ]
            ).content
