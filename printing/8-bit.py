# Here we are going to print out the colors using ANSI escape code (8-bit)

def run():
    print("Standard colors\n")
    for i in range(8):
        print(f"\x1b[48;5;{i};38;5;0m  {i}  \x1b[0m", end=" ")

    print("\n\nHigh-intensity colors\n")
    for i in range(8, 16):
        print(f"\x1b[48;5;{i};38;5;0m  {i}  \x1b[0m", end=" ")

    print("\n\n216 colors\n")
    for i in range(16, 232):
        print(f"\x1b[48;5;{i};38;5;0m {i} \x1b[0m", end="")

    print("\n\nGrayscale colors\n")
    for i in range(232, 256):
        print(f"\x1b[48;5;{i};38;5;0m {i} \x1b[0m", end="")


if __name__ == '__main__':
    run()
