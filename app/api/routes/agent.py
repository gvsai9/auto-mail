from fastapi import APIRouter

from app.agent.manual_agent import ManualAgent
from app.api.schemas.agent import (
    AgentRequest,
    AgentResponse,
)


router = APIRouter(
    prefix="/agent",
    tags=["Agent"],
)


@router.post(
    "/chat",
    response_model=AgentResponse,
)
def chat(request: AgentRequest):

    agent = ManualAgent()

    result = agent.invoke(
        request.message
    )

    response = result["response"]

    return AgentResponse(
        response=response.content
    )