def greet(name: str = "world") -> str:
    """Return a greeting for name."""
    return f"Hello, {name}!"

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Greet someone.")
    parser.add_argument("-n", "--name", default="world", help="Name to greet")
    args = parser.parse_args()
    print(greet(args.name))