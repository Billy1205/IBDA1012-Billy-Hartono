import os; os.system("cls")

text, word_count = [], {}
with open("Teks Kode 1b.txt", "r") as word_text:
    read_text = word_text.readlines()
    for row in read_text:
        row = row.split(" ")
        for word in row:
            word = word.strip("\n").strip(",").strip(".").strip(";").strip(":").strip("?").strip("!")
            text.append(word)
            word_count[word] = word_count.get(word, 0) + 1

print(f"All word count: {len(text)}")

print_count = sorted(word_count.items(), key=lambda x:x[1], reverse=True)
print("Top ten most repeated word:")
for key, value in print_count[:10]:
    print(f"{key}: {value} times")