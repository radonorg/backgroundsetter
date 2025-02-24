import os
import ctypes
import urllib.request

def download_image(url, save_path):
    try:
        urllib.request.urlretrieve(url, save_path)
        print(f"Desktop background downloaded to: {save_path}")
    except Exception as e:
        print(f"Failed to download desktop background: {e}")

def set_wallpaper(image_path):
    try:
        result = ctypes.windll.user32.SystemParametersInfoW(20, 0, image_path, 3)
        if result:
            print("Task completed.")
        else:
            print("Task failed.")
    except Exception as e:
        print(f"Error setting background: {e}")

def main():
    url = "https://raw.githubusercontent.com/radonorg/backgroundsetter/refs/heads/main/radon.png"
    pictures_folder = os.path.join(os.environ['USERPROFILE'], "Pictures")
    save_path = os.path.join(pictures_folder, "DesktopBackground.png")
    download_image(url, save_path)
    set_wallpaper(save_path)

if __name__ == "__main__":
    main()