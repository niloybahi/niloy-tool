import os
import sys
import time

def clear_screen():
    os.system("clear")

def banner():
    clear_screen()
    # CYBER NILOY BIG BANNER
    print("\033[1;31m")
    print(r"""
  ██████╗██╗   ██╗██████╗ ███████╗██████╗     ███╗   ██╗██╗██╗      ██████╗ ██╗   ██╗
 ██╔════╝╚██╗ ██╔╝██╔══██╗██╔════╝██╔══██╗    ████╗  ██║██║██║     ██╔═══██╗╚██╗ ██╔╝
 ██║      ╚████╔╝ ██████╔╝█████╗  ██████╔╝    ██╔██╗ ██║██║██║     ██║   ██║ ╚████╔╝ 
 ██║       ╚██╔╝  ██╔══██╗██╔══╝  ██╔══██╗    ██║╚██╗██║██║██║     ██║   ██║  ╚██╔╝   
 ╚██████╗   ██║   ██████╔╝███████╗██║  ██║    ██║ ╚████║██║███████╗╚██████╔╝   ██║    
  ╚═════╝   ╚═╝   ╚═════╝ ╚══════╝╚═╝  ╚═╝    ╚═╝  ╚═══╝╚═╝╚══════╝ ╚═════╝    ╚═╝    
    """)
    print("\033[1;36m=================================================================\033[0m")
    print("\033[1;33m             CYBER SECURITY & UTILITY TOOL v2.0                  \033[0m")
    print("\033[1;35m                 Owner: NILOY (niloybahi)                        \033[0m")
    print("\033[1;36m=================================================================\033[0m\n")

def calculator():
    banner()
    print("\033[1;34m--- Simple Calculator ---\033[0m\n")
    try:
        num1 = float(input("Enter first number: "))
        operator = input("Enter operator (+, -, *, /): ")
        num2 = float(input("Enter second number: "))

        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            result = num1 / num2
        else:
            result = "Invalid Operator!"

        print(f"\n\033[1;32mResult: {result}\033[0m")
    except Exception:
        print("\n\033[1;31mInvalid Input!\033[0m")
    
    input("\n\033[1;33mPress Enter to return to main menu...\033[0m")

def system_info():
    banner()
    print("\033[1;34m--- System Information ---\033[0m\n")
    print("[+] Platform: Termux")
    print("[+] Python Version:", sys.version.split()[0])
    print("[+] Tool Name: CYBER NILOY")
    print("[+] Developer: Niloy (niloybahi)")
    input("\n\033[1;33mPress Enter to return to main menu...\033[0m")

def main():
    while True:
        banner()
        print("\033[1;32m[1] Use Calculator\033[0m")
        print("\033[1;32m[2] View System Info\033[0m")
        print("\033[1;31m[0] Exit\033[0m\n")
        
        choice = input("\033[1;33mSelect an option (1/2/0): \033[0m")
        
        if choice == "1":
            calculator()
        elif choice == "2":
            system_info()
        elif choice == "0":
            print("\n\033[1;31mThank you for using! Goodbye.\033[0m")
            break
        else:
            print("\n\033[1;31m[-] Invalid Option! Please choose a valid number.\033[0m")
            time.sleep(1.5)

if __name__ == "__main__":
    main()
