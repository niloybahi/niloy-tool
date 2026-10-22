import os
import time

def clear_screen():
    os.system("clear")

def banner():
    clear_screen()
    print("\033[1;32m============================================\033[0m")
    print("\033[1;33m          WELCOME TO NILOY TOOL             \033[0m")
    print("\033[1;36m       Created by: Niloy (niloybahi)        \033[0m")
    print("\033[1;32m============================================\033[0m\n")

def main():
    banner()
    print("\033[1;35m[1] Introduce Yourself")
    print("[2] View System Information")
    print("[3] My GitHub Profile Info")
    print("[0] Exit\033[0m\n")
    
    choice = input("\033[1;33mSelect your choice (1/2/3/0): \033[0m")
    
    if choice == "1":
        name = input("\n\033[1;32mWhat is your name? \033[0m")
        print(f"\033[1;36m\nThank you {name}! Welcome to Niloy Tool.\033[0m")
    elif choice == "2":
        print("\n\033[1;32m[+] Tool Version: 1.0.0")
        print("[+] Platform: Termux (Python 3)\033[0m")
    elif choice == "3":
        print("\n\033[1;34m[+] Owner: Niloy")
        print("[+] GitHub: https://github.com/niloybahi\033[0m")
    elif choice == "0":
        print("\n\033[1;31mThank you! See you again.\033[0m")
        exit()
    else:
        print("\n\033[1;31m[-] Invalid option selected!\033[0m")

if __name__ == "__main__":
    main()
