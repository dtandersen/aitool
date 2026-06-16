import sys
from .command import ChatCommand
from .client import OpenAiClient


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: aitool <prompt>")
        sys.exit(1)

    prompt = " ".join(sys.argv[1:])
    client = OpenAiClient(
        api_key="ollama",
        base_url="http://localhost:11434/v1",
        default_model="llama3"
    )

    command = ChatCommand(client=client)
    command.execute(model=client.default_model, prompt=prompt)


if __name__ == "__main__":
    main()
