import os

def rename_files_in_directory(directory, prefix):
    try:
        files = os.listdir(directory)
        for file in files:
            old_path = os.path.join(directory, file)
            if os.path.isfile(old_path):  
                new_name = f"{prefix}_{file}"
                new_path = os.path.join(directory, new_name)
                os.rename(old_path, new_path)
                print(f"Renombrado: {file} -> {new_name}")
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    directory = input("Introduce el directorio con los archivos: ")
    prefix = input("Introduce el prefijo para los archivos: ")
    rename_files_in_directory(directory, prefix)
