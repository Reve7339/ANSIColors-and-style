# Here we are going to print out the styles using ANSI escape code

def run():
    for i in range(6):
        print(f"\x1b[{i}mStyle number {i}\x1b[0m\n")


if __name__ == '__main__':
    run()
