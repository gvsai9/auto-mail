from app.agent.manual_agent import ManualAgent

def test_agent_can_choose_read_tool():

    agent = ManualAgent()

    response = agent.invoke(
        "Read email mail_001"
    )

    print(response.tool_calls)

    assert response.tool_calls
    assert response.tool_calls[0]["name"] == "read_email"
def test_agent_can_choose_search_tool():

    agent = ManualAgent()

    response = agent.invoke(
        "Read my emails about the ML assignment"
    )

    print(response.tool_calls)

    assert response.tool_calls
    assert response.tool_calls[0]["name"] == "search_emails"
