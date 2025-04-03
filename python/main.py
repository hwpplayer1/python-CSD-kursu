import platform
import distro

def detect_os():
    os_name = platform.system()
    if os_name == "Linux":
        linux_dist = distro.name()
        linux_version = distro.version()
        print(f"Operating System: GNU/Linux")
        print(f"Distribution: {linux_dist}")
        print(f"Version: {linux_version}")
    else:
        print(f"Operating System: {os_name}")

if __name__ == "__main__":
    detect_os()