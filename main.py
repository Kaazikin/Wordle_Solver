from collections import Counter


def norm(n):
    return (n - 0.07) / (12.02 - 0.07)


def unique_chars(string):
    # Counting frequency
    return len(Counter(string))


def check_string(string, green, yellow, invalid):
    for b in green.keys():
        if string[b] != green[b]:
            return False
    for b in yellow:
        if b not in string:
            return False
    for b in invalid:
        if b in string:
            return False
    return True


letters = {"E": norm(12.02), "T": norm(9.1), "A": norm(8.12), "O": norm(7.68), "I": norm(7.31), "N": norm(6.95),
           "S": norm(6.28), "R": norm(6.02), "H": norm(5.92), "D": norm(4.32), "L": norm(3.98), "U": norm(2.88),
           "C": norm(2.71), "M": norm(2.61), "F": norm(2.30), "Y": norm(2.11), "W": norm(2.09), "G": norm(2.03),
           "P": norm(1.82), "B": norm(1.49), "V": norm(1.11), "K": norm(0.69), "X": norm(0.17), "Q": norm(0.11),
           "J": norm(0.10), "Z": norm(0.07)}
five_letter = {}
words = open("twl06.txt")
letters_yellow = []
letters_green = {}
for i in range(5):
    user_in = input("Input green letter for slot " + str(i + 1) + " or 0 for next slot.").upper()
    if user_in != "0":
        letters_green[i] = user_in

end = 0
while end < 6:
    letters_yellow.append(input("Input a yellow letter, 0 to exit").upper())
    if letters_yellow[-1] == str(0):
        letters_yellow.remove("0")
        end = 6
    else:
        end += 1

letters_invalid = []
end = 0
while end < 26:
    letters_invalid.append(input("Input a grey letter, 0 to exit").upper())
    if letters_invalid[-1] == str(0):
        letters_invalid.remove("0")
        end = 26
    else:
        end += 1

for x in words:
    y = x.strip("\n")
    if len(y) != 5:
        pass
    elif check_string(y.upper(), letters_green, letters_yellow, letters_invalid):
        s = 0
        for a in y.upper():
            s += letters[a]
        s *= unique_chars(y)
        five_letter[y.upper()] = s

words.close()
f = open("output_file.txt", "w")
for words in sorted(five_letter.items(), key=lambda item: item[1], reverse=True):
    f.write(str(words) + "\n")
f.close()

print("Successful. Check output.txt for full info. \n Top Results: \n")
print("=" * 20 + "\n")
print()

