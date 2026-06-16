import os
import typer
from dotenv import load_dotenv
from rich.console import Console
from aitool.command import ChatCommand
from aitool.client import OpenAiClient, OpenAiClientConfig

load_dotenv()
app = typer.Typer(no_args_is_help=False, rich_markup_mode=None)
console = Console()


@app.callback(invoke_without_command=True)
def callback(ctx: typer.Context):
    """
    aitool - AI CLI utility
    """
    config = OpenAiClientConfig(
        api_key=os.getenv("AITOOL_API_KEY", "ollama"),
        endpoint=os.getenv("AITOOL_ENDPOINT", "http://localhost:11434/v1"),
        model=os.getenv("AITOOL_MODEL", "llama3"),
    )
    ctx.obj = OpenAiClient(config=config)

    if ctx.invoked_subcommand is None:
        client = ctx.obj
        command = ChatCommand(client=client)
        console.print(
            "[bold blue]Interactive Chat Started[/bold blue] (Press Ctrl+C to exit)"
        )

        while True:
            try:
                user_input = typer.prompt("You", prompt_suffix=" > ")

                response = command.execute(model=client.config.model, prompt=user_input)
                console.print(f"[bold green]AI:[/bold green] {response}")

            except (typer.Abort, KeyboardInterrupt):
                break
        
        console.print("\n[yellow]Goodbye![/yellow]")
