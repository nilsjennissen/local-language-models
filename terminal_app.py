# Running ollama terminal app in the terminal:

import ollama
import rich
from rich.console import Console


# Terminal application that waits for user input and uses ollama to generate a response
def terminal_app():
    console = Console()
    console.print("Welcome to the Ollama terminal app!")
    console.print("Type 'exit' to quit the app.")
    while True:
        user_input = input("You: ")
        if (
            user_input == "exit"
            or user_input == "quit"
            or user_input == "q"
            or user_input == "x"
        ):
            console.print("Goodbye!")
            break
        else:
            response = ollama.chat(
                "mistral",
                messages=[
                    {"role": "user", "content": user_input},
                ],
            )
            response = response["message"]["content"]
            console.print(f"AI: {response}", style="#af00ff")


terminal_app()
