from Core_Lib.ILLMAdapter.LLMAdapter import LLMAdapter
from Core_Lib.ILLMAdapter.LLMAdapterModel import GeneratedResponse
from typing import List
from ollama import chat
from ollama import GenerateResponse
import ollama
from typing import Optional


class T100XAgent(LLMAdapter):

    def GenerateResponse(self, promt: str, agentName: Optional[str] = None) -> "GeneratedResponse":

        if not promt:
            raise ValueError("prompt Cannot be empty")

        if not agentName:
            agentName = self.GetSupportedAgents().pop()

        response: GenerateResponse = ollama.generate(
            model=agentName, prompt=promt, stream=False)

        return GeneratedResponse(reponse=response.response)

    def GetSupportedAgents(self) -> List[str]:

        self.__localModels: list = [local_llm["model"]
                                    for local_llm in ollama.list()["models"] if True]

        return self.__localModels
