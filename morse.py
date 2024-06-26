morse_dict = {
    "a": "._",
    "b": "_...",
    "c": "_._.",
    "d": "_..",
    "e": ".",
    "f": ".._.",
    "g": "__.",
    "h": "....",
    "i": "..",
    "j": ".___",
    "k": "_._",
    "l": "._..",
    "m": "__",
    "n": "_.",
    "o": "___",
    "p": ".__.",
    "q": "__._",
    "r": "._.",
    "s": "...",
    "t": "_",
    "u": ".._",
    "v": "..._",
    "w": ".__",
    "x": "_.._",
    "y": "_.__",
    "z": "__..",
    "1": ".____",
    "2": "..___",
    "3": "...__",
    "4": "...._",
    "5": ".....",
    "6": "_....",
    "7": "__...",
    "8": "___..",
    "9": "____.",
    "0": "_____"
}


def text_to_morse():
    text = input("Insert your text to convert to morse: ").strip(' ')
    morse_text = [morse_dict[letter] for letter in text if letter != " "]
    x = " ".join(morse_text)
    return x


if __name__ == "__main__":
    on = True
    while on:
        result = text_to_morse()
        choice = input(f"{result}\nDo you wanna try again? Y/N: ").lower()
        if choice == "n":
            on = False
