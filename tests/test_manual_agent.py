from app.agent.manual_agent import ManualAgent


def test_manual_agent_search():

    agent = ManualAgent()

    response = agent.invoke(
        "Find my emails about the ML assignment."
    )

    print("\nFINAL RESPONSE:")
    print(response)

    assert response.content