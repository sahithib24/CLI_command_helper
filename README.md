# CLI Command Helper ⚡️

A lightweight terminal tool that generates Linux/macOS commands using natural language queries. Designed for developers who want to save time on command syntax lookup.

## Features
- 🔍 **Natural Language Processing**: Ask for commands in plain English (e.g., "how to delete all Docker containers")
- 🖥️ **Multi-Platform Support**: Works with common command-line tools (Git, Docker, AWS CLI, etc.)
- 🤖 **AI-Powered**: Uses Ollama (local) or OpenAI to generate accurate commands
- ⚡ **Instant Results**: Get commands without leaving your terminal

## Installation
1. Install Python 3.10+
2. Install dependencies:
```bash
pip install click requests python-dotenv
```
3. For local AI:
```bash
ollama pull llama3  # Requires Ollama installation
```

## Usage
```bash
python cli_helper.py --how-to "your query"
```
Example:
```bash
python cli_helper.py --how-to "list all git branches sorted by date"
```

## Tech Stack
- Python 3
- Ollama/OpenAI
- Click (CLI framework)
