import os

path = "/home"

for folder in os.listdir(path):
    folder_path = os.path.join(path, folder)

    if os.path.isdir(folder_path):
        size = sum(
            os.path.getsize(os.path.join(dp, f))
            for dp, dn, filenames in os.walk(folder_path)
            for f in filenames
        )

        print(f"{folder}: {size / (1024**2):.2f} MB")
