def main():
    try:
        filename = input("Enter filename: ")
        with open(filename, 'r') as file:
            lines = file.readlines()

        if not lines:
            print("The file is empty.")
            return

        while True:
            print(f"\nThe file has {len(lines)} lines.")
            try:
                line_number = int(input("Enter a line number (0 to quit): "))

                if line_number == 0:
                    print("Goodbye!")
                    break
                elif 1 <= line_number <= len(lines):
                    print(f"Line {line_number}: {lines[line_number - 1].rstrip()}")
                else:
                    print(f"Invalid line number. Please enter a number from 1 to {len(lines)}.")

            except ValueError:
                print("Please enter a valid integer.")

    except FileNotFoundError:
        print("File not found. Please check the filename and try again.")

if __name__ == "__main__":
    main()
