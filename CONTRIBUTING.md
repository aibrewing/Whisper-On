# Contributing

Contributions are welcome! Here's how to get involved.

## Reporting bugs

Open an issue with:
- Your Windows version
- Python version (`python --version`)
- The full error message from the terminal
- Steps to reproduce

## Suggesting features

Open an issue tagged `enhancement` with a clear description of the use case.

## Submitting a pull request

1. Fork the repo
2. Create a branch: `git checkout -b feature/your-feature-name`
3. Make your changes
4. Test manually (run `transcriber.py` and verify hotkey + UI work)
5. Submit a pull request with a clear description of what changed and why

## Code style

- Python: follow PEP 8, keep functions small and focused
- HTML/JS: vanilla only (no frameworks), keep the single-file structure
- Comments: explain *why*, not *what*

## Important: never commit `config.json` or `history.json`

These files contain your personal API key and transcript data.
They are excluded in `.gitignore` — keep it that way.
