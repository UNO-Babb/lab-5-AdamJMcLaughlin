import os

def countLetters(message):
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    message = message.upper()

    freq = [0] * 26  # Initialize frequency list

    # Count each letter's frequency
    for char in message:
        if char in alpha:
            position = alpha.index(char)
            freq[position] += 1

    # Create CSV output
    output = ""
    for i in range(26):
        print(alpha[i], ":", freq[i])
        line = alpha[i] + "," + str(freq[i]) + "\n"
        output += line

    writeToFile(output)


def writeToFile(fileText):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    os.chdir(dir_path)

    with open("frq.csv", 'w') as freqFile:
        freqFile.write(fileText)

    print("Frequencies saved to 'frq.csv'. You can now open it in Excel to create a chart.")


def main():
    msg = input("Enter a message: ")
    countLetters(msg)

main()
