if __name__ == "__main__":
    for x in range(30):
        print("{}".format(("buzz" if x % 2 == 0 else "") + ("fizz" if x % 3 == 0 else "") + ("lol" if x % 5 == 0 else "")) or x)
