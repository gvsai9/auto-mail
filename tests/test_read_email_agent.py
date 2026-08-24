from app.agent.manual_agent import ManualAgent


def test_agent_read_email():

    agent = ManualAgent()

    response = agent.invoke(
        "Read the email about the ML assignment and tell me what the deadline is."
    )

    print("\n===== AGENT READ RESPONSE =====")
    print(response)
    print("================================\n")

    assert response is not None