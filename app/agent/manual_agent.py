from langchain_core.messages import (
    HumanMessage,
    SystemMessage,
    ToolMessage,
)

from app.composition.dependencies import (
    create_llm,
    create_tool_registry,
    create_tool_executor,
)


class ManualAgent:

    def __init__(self, credentials):

        self.model = create_llm()

        self.registry = create_tool_registry(
            credentials
        )

        self.executor = create_tool_executor(
            credentials
        )

        self.tool_calls = []

        self.model = self.model.bind_tools(
            self.registry.get_all()
        )

    def invoke(
        self,
        user_input: str,
    ):

        messages = [
            SystemMessage(
                content="""
You are an email assistant.

You have tools for searching, reading, and sending emails.

READING EMAILS:

- If the user asks to read, inspect, summarize, or answer something
  about an email and does not provide an exact email ID,
  you MUST call the `search_emails` tool FIRST.

- Use the user's description as the search query.

- `search_emails` returns email results containing their exact IDs.

- After receiving the `search_emails` result, inspect the result
  and take the exact ID of the relevant email.

- Then call `read_email` using that exact ID.

- NEVER call `read_email` first when the user has not provided
  an exact email ID.

- NEVER use "search_email", "search_emails", a description,
  a query, or a placeholder as the ID for `read_email`.

- `read_email` accepts ONLY a real email ID.

If the user explicitly gives an exact email ID, you may call
`read_email` directly.

SEARCHING EMAILS:

- Use `search_emails` to find emails based on keywords,
  subject, content, sender, or a description.

SENDING EMAILS:

- Use `send_email` when the user asks to compose or send an email.
- The `send_email` tool only prepares the email.
- NEVER assume the email has been sent.
- The user must explicitly confirm before the email is sent.
"""
            ),
            HumanMessage(
                content=user_input
            ),
        ]

        generated_email = None

        while True:

            response = self.model.invoke(
                messages
            )

            print(
                "\n===== LLM RESPONSE ====="
            )
            print(response)
            print(
                "========================\n"
            )

            messages.append(response)

            # LLM is finished
            if not response.tool_calls:

                return {
                    "response": response,
                    "email": generated_email,
                }

            # Execute requested tools
            for tool_call in response.tool_calls:

                result = self.executor.execute(
                    tool_call
                )

                print(
                    "\n===== TOOL RESULT ====="
                )
                print(result)
                print(type(result))
                print(
                    "=======================\n"
                )

                # Capture generated email
                if tool_call["name"] == "send_email":

                    generated_email = result["email"]

                messages.append(
                    ToolMessage(
                        content=str(result),
                        tool_call_id=tool_call["id"],
                    )
                )