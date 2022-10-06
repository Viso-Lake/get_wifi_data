import subprocess

def extract_wifi_passwords():
    profiles_data = subprocess.check_output('netsh wlan show profiles').decode('cp866').split('\n')
    profiles = []
    
    for i in profiles_data:
        if 'All User Profile' in i:
            profiles.append(i.split(':')[1].strip())
        elif 'Все профили пользователей' in i:
            profiles.append(i.split(':')[1].strip())
    
    with open('wifi_passwords.txt', 'w') as f:
        for profile in profiles:
                f.writelines(f'Логин: {profile}\n')
                profile_info = subprocess.check_output(f'netsh wlan show profile {profile} key=clear').decode('cp866').split('\n')
                try:
                    password = []
                    for i in profile_info:
                        if 'Key Content' in i:
                            password.append(i.split(':')[1].strip())
                        elif 'Содержимое ключа' in i:
                            password.append(i.split(':')[1].strip())
                    f.write(f'Пароль: {password[0]}\n\n')
                except IndexError:
                    password = None
                    f.write('Нет пароля\n\n')
                    
                if password is not None:
                    print(f'Profile: {profile}\nPassword: {password[0]}\n\n')
                else:
                    print(f'Profile: {profile}\nPassword: \n\n')
                
    print("ALL DATA SAVED IN FILE wifi_passwords.txt")
        

extract_wifi_passwords()