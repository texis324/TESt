"""Simple greeting utility with CLI support."""

from __future__ import annotations

import argparse


def greet(name: str | None = None) -> str:
    """Return a friendly Japanese greeting.

    Args:
        name: Optional name to include in the greeting.
    """
    if name:
        return f"こんにちは、{name}さん！"
    return "こんにちは！"


def build_parser() -> argparse.ArgumentParser:
    """Create an argument parser for the greeting CLI."""
    parser = argparse.ArgumentParser(description="Print a Japanese greeting")
    parser.add_argument("name", nargs="?", help="Optional name to greet")
    return parser


def main() -> None:
    """CLI entry point."""
    parser = build_parser()
    args = parser.parse_args()
    print(greet(args.name))


if __name__ == "__main__":
    main()
