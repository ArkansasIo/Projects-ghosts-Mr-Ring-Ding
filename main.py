from agent.agent import CartoonAgent


def main():
    agent = CartoonAgent()
    world = "A whimsical blue cartoon studio with doors, switches, a window, and movable props."

    print("Ring-A-Ding AI is online. Type 'quit' to exit.")
    while True:
        user = input("\nYou: ").strip()
        if user.lower() in {"quit", "exit"}:
            break

        result = agent.chat(user, world_context=world)
        print(f"Ring-A-Ding: {result['text']}")
        print(
            f"[emotion={result['emotion']} gesture={result['gesture']} "
            f"world_action={result['world_action']}]"
        )


if __name__ == "__main__":
    main()
