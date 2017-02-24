from Swapping import Swapping

def main():
    swapper = Swapping()

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

            elif response[0] == "bf":
                if len(response) == 2:
                    pid = response[1]

            elif response[0] == "wf":
                if len(response) == 2:
                    pid = response[1]

            elif response[0] == "de":
                if len(response) == 2:
                    pid = response[1]

            elif response[0] == "quit":
                break
            else:
                print("Unknown command")

if __name__ == '__main__':
    main()