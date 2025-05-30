from Core_Lib.LLMInteropLibrary import LLMAgentProvider, AgentGenerate
from Core_Lib.T100XLLMAgent.T100XAgent import T100XAgent


# init DI
LLMagent = T100XAgent()
LLMAgentProvider.LLMAgentProvider.register_agent(LLMagent)


AgentGenerate.AgentGenerate().GenerateResponse(
    "what if you fail to kill jhon cornnor")
