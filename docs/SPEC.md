# aitool Specification

## 1. Overview
`aitool` is a lightweight CLI utility for interacting with OpenAI-compatible APIs. It is built using Spec-Driven Development (SDD) principles, ensuring that the implementation strictly adheres to defined data models.

## 2. Core Requirements
- **Endpoint Compatibility**: Support any OpenAI-compliant API (e.g., OpenAI, Ollama, vLLM, LocalAI, Anthropic via proxy).
- **Configuration**: Support persistent settings via file (`~/.config/aitool/config.yaml`) and overrides via environment variables.
- **User Interface**: Provide a modern terminal experience with Markdown rendering and streaming support.

## 3. Command Line Interface
- `aitool chat [PROMPT]`: 
    - `--model, -m`: Specify the model (overrides default).
    - `--system, -s`: Provide a custom system instruction.
    - `--no-stream`: Disable real-time output (default is streaming).
- `aitool config`: 
    - `set <KEY> <VALUE>`: Persist a setting.
    - `list`: Show current resolved configuration.
- `aitool exec <PROMPT>`: 
    - Non-interactive mode optimized for shell piping and scripting.

## 4. Data Models (The "Spec")
The tool's behavior is driven by simple data structures.


## 5. Command Classes
The core logic is encapsulated in command classes:
- **`ChatCommand`**:
    - **Attributes**: `prompt: str`, `config: ConfigModel`
    - **Methods**: `execute() -> None`
    - **Behavior**: Initializes an OpenAI client, sends the prompt to the configured model, and streams the output directly to the terminal using `Rich`.

## 6. Technical Stack
- **Runtime**: Python 3.14+
- **CLI Framework**: `Typer` (for type-safe command handling).
- **API Client**: `openai` (for standard protocol compatibility).
- **Formatting**: `rich` (for Markdown rendering and progress spinners).
