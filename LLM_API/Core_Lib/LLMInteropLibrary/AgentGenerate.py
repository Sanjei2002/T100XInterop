from collections.abc import Iterator
from Core_Lib.ILLMAdapter.LLMAdapterModel import GeneratedResponse
from Core_Lib.LLMInteropLibrary.LLMAgentProvider import LLMAgentProvider
from typing import Optional


class AgentGenerate:

    def GenerateResponse(self, promt: str, agentIndx=0) -> Iterator[str]:

        if not promt:
            raise ValueError()

        if agentIndx >= len(self.GetAgentsList()):
            raise IndexError()

        responseStream: Iterator[GeneratedResponse] = LLMAgentProvider.get_agent().GenerateResponse(
            promt=promt, agentName=self.GetAgentsList()[agentIndx], streamResponse=True)

        for chunk in responseStream:
            yield chunk.Value

       # return (response.Value for response in responseStream)

    def GetAgentsList(self) -> list[str]:
        return LLMAgentProvider.get_agent().GetSupportedAgents()
