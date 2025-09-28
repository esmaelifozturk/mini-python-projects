def note_app():
    note = input("Notunuzu yazınız: ")
    with open("notes.txt", "a", encoding="utf-8") as f:
        f.write(note + "\n")
    print("Not kaydedildi.")

    print("\nMevcut Notlar:")
    with open("notes.txt", "r", encoding="utf-8") as f:
        for line in f:
            print(line.strip())

note_app()
