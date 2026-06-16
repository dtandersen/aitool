import sys
from .models import ConfigModel
from .commands import ChatCommand
from .client import OpenAiClient

def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: aitool <prompt>")
        sys.exit(1)
    
    prompt = " ".join(sys.argv[1:])
    config = ConfigModel()
    client = OpenAiClient(config)
    
    command = ChatCommand(client=client)
    command.execute(prompt=prompt)

if __name__ == "__main__":
    main()
