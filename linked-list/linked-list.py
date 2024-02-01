def main():

    linked_list = {
        # <memory location>: <[<data>, <pointer to next memory location>]>
        # memory location is the key and the value is the lsit of the other 2 things

        1: ["node a", 2],
        2: ["node b", 3],
        3: ["node c", 4],
        4: ["node d", None],
    }

    print(linked_list[1])
    print(f"{linked_list[1][0]} links to {linked_list[1][1]}")


if __name__ == '__main__':
    main()
