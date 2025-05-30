from abc import ABC, abstractmethod
from Core_Lib.ILLMAdapter.LLMAdapterModel import GeneratedResponse
from typing import List, Optional


class LLMAdapter(ABC):

    @abstractmethod
    def GenerateResponse(self, promt: str, agentName:  Optional[str] = "") -> "GeneratedResponse":
        """
        if agentName is not given default Agent will be used
        prompt  : instruction for the LLM
        """
        pass

    @abstractmethod
    def GetSupportedAgents(self) -> List[str]:
        pass
