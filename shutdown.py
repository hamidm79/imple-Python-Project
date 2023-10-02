import os
print("A)Shutdown\nB)Restart\nC)Cancel")
choice=input("what is your choice?")
if choice =='A':
    print("shutting down...")
    os.system("shutdwon /s /t 5")
elif choice == 'B':
    print("restarting...")
    os.system("shutdown /r /t 5")
elif choice == "C":
    print("canceled!")
    exit()
else:
    print("wrong choice!")