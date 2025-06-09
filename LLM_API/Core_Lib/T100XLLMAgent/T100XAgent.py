from urllib import response
from Core_Lib.ILLMAdapter.LLMAdapter import LLMAdapter
from Core_Lib.ILLMAdapter.LLMAdapterModel import GeneratedResponse
from typing import List
from ollama import chat
from ollama import GenerateResponse
import ollama
from typing import Optional, Iterator


class T100XAgent(LLMAdapter):

    def GenerateResponse(self, promt: str, agentName: Optional[str] = None, streamResponse=False) -> Iterator[GeneratedResponse]:

        if not promt:
            raise ValueError("prompt Cannot be empty")

        if not agentName:
            agentName = self.GetSupportedAgents().pop()

        stream: GenerateResponse | Iterator[GenerateResponse] = ollama.generate(
            model=agentName, prompt=promt, stream=streamResponse)

        # with open("Interop.log", "w") as logfile:

        #     for chunk in stream:
        #         print(chunk.response, sep="", file=logfile, flush=True)   # type: ignore

        if streamResponse:
            # Return a generator expression yielding GeneratedResponse objects
            # type: ignore
            for chunk in stream:
                response: str = chunk.response  # type: ignore

                if response:
                    yield GeneratedResponse(response=response)
        else:
            yield GeneratedResponse(response=stream.response)  # type: ignore

    def GetSupportedAgents(self) -> List[str]:

        self.__localModels: list = [local_llm["model"]
                                    for local_llm in ollama.list()["models"] if True]

        return self.__localModels
