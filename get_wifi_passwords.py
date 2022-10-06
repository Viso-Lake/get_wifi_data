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
                    password = [i.split(':')[1].strip() for i in profile_info if 'Key Content' in i][0]
                    f.write(f'Пароль: {password}\n\n')
                except IndexError:
                    password = None
                    f.write('Пароль: None \n\n')
                print(f'Profile: {profile}\nPassword: {password}\n\n')
                
    print("ALL DATA SAVED IN FILE wifi_passwords.txt")
        

extract_wifi_passwords()