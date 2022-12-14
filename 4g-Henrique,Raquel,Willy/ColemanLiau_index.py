def colemanLiau(text=''):
    if text != '':
        x = text
    else:
        x = input("Digit your text: ")
    # Number of words
    w = 1
    for i, a in enumerate(x):
        if i != 0:
            if a == " " and x[i-1] != " ":
                w = w + 1

    # Number of sentences
    s = 0
    for b in x:
        if b == "." or b == "!" or b == "?":
            s = s + 1

    # Number of letters
    l = 0
    for c in x:
        # PYTHON Documentation (Utilities for ASCII characters - that check all letters lower and upper -)
        if c.isalpha():
            l = l + 1

    # Coleman-Liau index
    cl = (l / w * 100)

    cs = (s / w * 100)

    calcu = round((0.0588 * cl) - (0.296 * cs) - 15.8)

    if text == '':
        # Print of the Before Grade 1
        if calcu < 1:
            print("Below Grade 1")

        # Print of the Grade 1
        if calcu == 1 or calcu > 1 and calcu < 16:
            print(f"Grade: {calcu}")

        # Print of the Grade mora then 16
        if calcu > 16:
            print("Grade 16+")

    return calcu


if __name__ == '__main__':
    colemanLiau()
