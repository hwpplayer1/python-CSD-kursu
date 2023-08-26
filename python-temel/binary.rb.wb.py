def copy_file(source_path, dest_path):
    with open(source_path, 'rb') as fs:
        with open(dest_path, 'wb') as fd:
            while True:
                b = fs.read(4096)
                if not b:
                    break
                fd.write(b)
copy_file('sample.py', 'test.txt')
