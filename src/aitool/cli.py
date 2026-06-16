import os
import typer
from dotenv import load_dotenv
from rich.console import Console
from aitool.command import ChatCommand
from aitool.client import OpenAiClient, OpenAiClientConfig

load_dotenv()
app = typer.Typer(no_args_is_help=True, rich_markup_mode=None)
console = Console()


@app.callback()
def callback(ctx: typer.Context):
    """
    aitool - AI CLI utility
    """
    config = OpenAiClientConfig(
        api_key=os.getenv("AITOOL_API_KEY", "ollama"),
        endpoint=os.getenv("AITOOL_ENDPOINT", "http://localhost:11434/v1"),
        model=os.getenv("AITOOL_MODEL", "llama3")
    )
    ctx.obj = OpenAiClient(config=config)


@app.command()
def chat(ctx: typer.Context, message: str):
    """Send a message and print the response."""
    client = ctx.obj
    command = ChatCommand(client=client)
    response = command.execute(model=client.config.model, prompt=message)
    console.print(response)
