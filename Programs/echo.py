def echo(text: str, repetitions: int = 3) -> str:
    """Imitate an echo"""
    echo_text = []
    for i in range(repetitions):
        echo_text = text[i - 3 :]  # takes the last 3 characters of the string
        print(echo_text)


if __name__ == "__main__":
    text = input("Yell something into the mountain: ")
    print(echo(text))
