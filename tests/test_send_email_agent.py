from app.agent.manual_agent import ManualAgent


def test_agent_send_email():

    agent = ManualAgent()

    result = agent.invoke(
        "Send an email to ravi@example.com saying that I completed the ML assignment."
    )


    print("\n===== AGENT RESPONSE =====")
    print(result["response"].content)

    print("\n===== GENERATED EMAIL =====")
    print(result["email"])

    assert result["response"] is not None