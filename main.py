import click
import requests

def ask_ollama(query):
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3",
            "prompt": f"Return ONLY the terminal command for: {query}. Do not explain.",
            "stream": False  # Explicitly disable streaming
        }
    )
    try:
        return response.json()["response"].strip()
    except KeyError:
        # Fallback for different response formats
        return response.json().get("message", {}).get("content", "").strip()

@click.command()
@click.option('--how-to', help='Ask for a command, e.g., "kill all Docker containers"')
def cli(how_to):
    if how_to:
        try:
            command = ask_ollama(how_to)
            click.echo(f"Command: {command}")
        except requests.exceptions.RequestException as e:
            click.echo(f"Error: {str(e)}", err=True)
    else:
        click.echo("Usage: cmdhelper --how-to 'your query'")

if __name__ == '__main__':
    cli()