import time
from typing import Iterable
from flask import Flask, Response, jsonify, abort, request
from Core_Lib.LLMInteropLibrary.AgentGenerate import AgentGenerate
from Core_Lib.LLMInteropLibrary.LLMAgentProvider import LLMAgentProvider
from Core_Lib.T100XLLMAgent.T100XAgent import T100XAgent
from collections import Counter

# init DI
LLMagent = T100XAgent()
LLMAgentProvider.register_agent(LLMagent)

app = Flask(__name__)


@app.route('/')
def index():
    return 'Supreme webONe UI!'


@app.get("/getAgentslist")
def GetAgentsList():

    agents_list = AgentGenerate().GetAgentsList()

    # Create numbered list strings
    numbered_agents = [f"{i}. {agent}" for i,
                       agent in enumerate(agents_list)]

    response = {"data": numbered_agents}
    return jsonify(response)


@app.post("/getPromptResponse")
def GenerateLLMResponse():

    try:
        if not request.form.get('content'):
            return "empty prompt", 400

        agentIdx = int(request.args.get("agentIdx", "0"))
        prompt: str = request.form.get("content", "")

        response = AgentGenerate().GenerateResponse(promt=prompt, agentIndx=agentIdx)

        return Response(response=response, status=200)

    except:
        abort(500, "")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
