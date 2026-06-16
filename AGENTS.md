# Agents Specification

## Critical Rules
- **Remote Push**: NEVER `git push` unless the user has explicitly typed "push" or confirmed a plan that includes pushing in the current turn. Combining `git push` into a batch command without an explicit confirmation for that specific action is strictly forbidden. Do not proactively ask the user if you should push; simply execute the push when the conditions above are met.
- **Commits**: NEVER `git commit` unless the user has explicitly requested it or confirmed a plan that includes committing. Do not proactively ask the user if you should commit; simply execute the commit when the conditions are met.
- **Testing**: This project uses `pytest` and `pyhamcrest`. Always verify changes with `uv run pytest`.

## Project Structure
- Source: `src/`
- Tests: `tests/`

