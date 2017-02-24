from Swapping import Swapping

def main():
    swapper = Swapping()


    # debug
    # swapper.listJobs()
    # swapper.add(1, 5)
    # swapper.listSegments()
    # swapper.firstFit(1)
    # swapper.listSegments()
    # swapper.add(2, 17)
    # swapper.firstFit(2)
    # swapper.listSegments()
    # swapper.deallocate(2)
    # swapper.listSegments()
    # swapper.firstFit(2)
    # swapper.listSegments()
    # swapper.deallocate(1)
    # swapper.listSegments()
    # swapper.add(3, 7)
    # swapper.firstFit(3)
    # swapper.listSegments()
    # swapper.add(4, 4)
    # swapper.listSegments()
    # swapper.firstFit(4)
    # swapper.listSegments()
    # swapper.deallocate(2)
    # swapper.listSegments()


    swapper.add(1, 5)
    swapper.add(2, 4)
    swapper.add(3, 3)
    swapper.add(4, 2)
    swapper.add(5, 1)






    while True:
        response = input("Enter a command: ")
        response = response.strip().split()

        if len(response) > 0:
            if response[0] == "add":
                if len(response) == 3:
                    pid = response[1]
                    size = response[2]
                    swapper.add(pid, size)

            elif response[0] == "jobs":
                swapper.listJobs()

            elif response[0] == "list":
                swapper.listSegments()

            elif response[0] == "ff":
                if len(response) == 2:
                    pid = response[1]
                    swapper.firstFit(pid)

            elif response[0] == "nf":
                if len(response) == 2:
                    pid = response[1]
                    swapper.nextFit(pid)

            elif response[0] == "bf":
                if len(response) == 2:
                    pid = response[1]
                    swapper.bestFit(pid)

            elif response[0] == "wf":
                if len(response) == 2:
                    pid = response[1]
                    swapper.worstFit(pid)

            elif response[0] == "de":
                if len(response) == 2:
                    pid = response[1]
                    swapper.deallocate(pid)

            elif response[0] == "quit":
                break
            else:
                print("Unknown command")

if __name__ == '__main__':
    main()