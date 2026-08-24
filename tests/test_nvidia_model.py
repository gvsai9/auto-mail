from app.composition.dependencies import create_llm


def test_nvidia_model():

    model = create_llm()

    response = model.invoke(
        "Reply with exactly: NVIDIA connection successful"
    )

    print("\nMODEL RESPONSE:")
    print(response)

    assert response.content