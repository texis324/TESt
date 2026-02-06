def greet(name=None):
    if name:
        return f"こんにちは、{name}さん！"
    return "こんにちは！"


if __name__ == "__main__":
    print(greet())
    print(greet("世界"))
