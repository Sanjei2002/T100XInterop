from Core_Lib.ILLMAdapter.LLMAdapter import LLMAdapter
from typing import Optional


class LLMAgentProvider:
    # Use single underscore to avoid name mangling but keep it "private"
    _llm_agent: Optional[LLMAdapter] = None

    @staticmethod
    def register_agent(agent: LLMAdapter):
        """
        Register the LLMAdapter instance to be returned by GetAgent.
        """
        LLMAgentProvider._llm_agent = agent

    @staticmethod
    def get_agent() -> LLMAdapter:
        """
        Return the registered LLMAdapter instance.
        Raise error if no agent has been registered.
        """
        if not LLMAgentProvider._llm_agent:
            raise NotImplementedError("No LLMAdapter has been registered yet.")
        return LLMAgentProvider._llm_agent
