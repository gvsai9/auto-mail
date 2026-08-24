

from app.agent.manual_agent import ManualAgent

def test_agent_direct_read():

    agent = ManualAgent()

    response = agent.invoke(
        "Read email email_001"
    )

    assert response is not None
    assert response.content

    tool_names = [
        call["name"]
        for call in agent.tool_calls
    ]

    assert tool_names == ["read_email"]

    assert agent.tool_calls[0]["args"]["id"] == "email_001"

    agent = ManualAgent()

    response = agent.invoke(
        "Read my email about the ML assignment."
    )

    assert response is not None
    assert response.content

    tool_names = [
        call["name"]
        for call in agent.tool_calls
    ]

    assert tool_names == [
        "search_emails",
        "read_email",
    ]

    read_calls = [
        call for call in agent.tool_calls
        if call["name"] == "read_email"
    ]

    assert read_calls[0]["args"]["id"] == "email_001"