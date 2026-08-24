from app.agent.manual_agent import ManualAgent


def test_agent_send_email():

    agent = ManualAgent()

    response = agent.invoke(
        "Send an email to ravi@example.com saying that I completed the ML assignment."
    )

    print("\n===== FINAL RESPONSE =====")
    print(response.content)

    assert response is not None
    assert response.content