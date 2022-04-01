# Here we are going to print out the colors using ANSI escape code (3-4-bit)

def run():
    for fg in range(30, 38):
        for bg in range(40, 48):
            print(f"\x1b[{fg};{bg}m{fg};{bg}\x1b[0m", end="  ")
        print("")


if __name__ == '__main__':
    run()
