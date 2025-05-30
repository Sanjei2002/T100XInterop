from Core_Lib.LLMInteropLibrary.LLMAgentProvider import LLMAgentProvider
from typing import Optional


class AgentGenerate:

    def GenerateResponse(self, promt: str, agentIndx=0) -> str:

        if not promt:
            raise ValueError()

        if agentIndx >= len(self.GetAgentsList()):
            raise IndexError()

        response = LLMAgentProvider.get_agent().GenerateResponse(
            promt=promt, agentName=self.GetAgentsList()[agentIndx])

        return response.Value

    def GetAgentsList(self) -> list[str]:
        return LLMAgentProvider.get_agent().GetSupportedAgents()
