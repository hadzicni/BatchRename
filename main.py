import os

def rename_files(directory, prefix, suffix):
    for filename in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, filename)):
            new_filename = prefix + filename + suffix
            old_filepath = os.path.join(directory, filename)
            new_filepath = os.path.join(directory, new_filename)
            os.rename(old_filepath, new_filepath)
            print(f"Datei '{filename}' wurde in '{new_filename}' umbenannt.")

if __name__ == "__main__":
    directory = input("Bitte gib den Verzeichnispfad an: ")
    prefix = input("Bitte gib das Präfix für die Dateinamen ein: ")
    suffix = input("Bitte gib das Suffix für die Dateinamen ein: ")
    rename_files(directory, prefix, suffix)
