import os

def detect_file_system():
    try:
        # Check the root directory's file system type
        os_info = os.uname()
        print(f"Operating System: {os_info.sysname}")
        if os_info.sysname == "Linux":
            print("Likely file system: ext4, ext3, or similar.")
        elif os_info.sysname == "Darwin":
            print("Likely file system: APFS or HFS+.")
        elif os_info.sysname == "Windows":
            print("Likely file system: NTFS or FAT32.")
        else:
            print("Unable to determine the file system type.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    detect_file_system()