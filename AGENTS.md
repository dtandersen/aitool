# Agents Specification

## Critical Rules
- **Remote Push**: NEVER `git push` unless the user has explicitly typed "push" or confirmed a plan that includes pushing in the current turn. Combining `git push` into a batch command without an explicit confirmation for that specific action is strictly forbidden.
- **Testing**: This project uses `pytest` and `pyhamcrest`. Always verify changes with `uv run pytest`.

## Project Structure
- Source: `src/`
- Tests: `tests/`

