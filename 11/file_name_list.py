def check_file_names(file_names):
    for file_name in file_names:
        name, ext = file_name.rsplit('.', 1)
        if name[0].isdigit():
            print(f"{file_name}: Error - Name starts with a number")
            continue
        if sum(c.isdigit() for c in name) > 3:
            print(f"{file_name}: Error - Name contains more than three numbers")
            continue
        if not (2 <= len(ext) <= 3) or any(c.isdigit() for c in ext):
            print(f"{file_name}: Error - Invalid extension")
            continue
        if ext == "err":
            print(f"{file_name}: Error - Extension cannot be 'err'")
            continue
        print(f"{file_name}: Acceptable")

file_names = ["file1.txt", "2file.txt", "file1234.txt", "file.err", "file.tx1"]
check_file_names(file_names)
