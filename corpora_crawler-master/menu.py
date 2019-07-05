import os
import sys
import time


def menu(start_time):
    print("\n")
    sys.stdout.write('\033[7m')
    sys.stdout.write('\33[32m')
    print("##############################################\n")
    sys.stdout.write('\033[0m')
    sys.stdout.write('\033[1m')
    sys.stdout.write('\033[94m')
    print(f"\nTook {int(time.time() - start_time)} seconds running\n")
    print("Wellcome to our Corpora Crawler project: \n \n Please press one option: \n \n 1. Run Program. \n 2. Create inicial dictionaries. \n 3. Run only crawler. \n 4. Run only urls processor. \n 5. Run only language identifier.\n 6. Run Help. \n 7. Clear terminal text (just menu). \n 8. Install external resources. \n\n\n 0. Exit Program. \n")
    sys.stdout.write('\033[7m')
    sys.stdout.write('\33[32m')
    print("##############################################\n")
    sys.stdout.write('\033[0m')
    choice = input()

    if choice == '1':
        bashCommand = 'clear'
        os.system(bashCommand)
        start_time = time.time()
        bashCommand = 'python3 bootstrap.py'
        os.system(bashCommand)
        bashCommand = 'python3 crawler.py'
        os.system(bashCommand)
        bashCommand = 'python3 processor.py'
        os.system(bashCommand)
        bashCommand = 'python3 identifier.py'
        os.system(bashCommand)

    if choice == "2":
        bashCommand = 'clear'
        os.system(bashCommand)
        bashCommand = 'python3 bootstrap.py'
        os.system(bashCommand)

    if choice == '3':
        bashCommand = 'clear'
        os.system(bashCommand)
        bashCommand = 'python3 crawler.py'
        os.system(bashCommand)

    if choice == '4':
        bashCommand = 'clear'
        os.system(bashCommand)
        bashCommand = 'python3 processor.py'
        os.system(bashCommand)

    if choice == '5':
        bashCommand = 'clear'
        os.system(bashCommand)
        bashCommand = 'python3 identifier.py'
        os.system(bashCommand)

    if choice == '6':#Fazer de maneira a so aparecer o help.
        bashCommand = 'clear'
        os.system(bashCommand)
        with open("help.txt", 'r') as f:
            print(f.read())
            f.close()

    # if choice == '7':
    #     bashCommand = 'clear'
    #     os.system(bashCommand)
    #     # print("Deleting Processor files.")
    #     # bashCommand = 'python3 delete_processed.py'
    #     # os.system(bashCommand)
    #     print("Deleting Unclassfied files and Unclassified urls.")
    #     bashCommand = 'python3 delete_querys_documents.py'
    #     os.system(bashCommand)
    #     # print("Deleting Query files.")
    #     # bashCommand = 'python3 delete_querys.py'
    #     # os.system(bashCommand)
    #     # print("Deleting GoodPotencial files.")
    #     # bashCommand = 'python3 delete_goodpotencial.py'
    #     # os.system(bashCommand)

    if choice == '7':
        bashCommand = 'clear'
        os.system(bashCommand)

    if choice == '8':
        os.system(bashCommand)
        bashCommand = 'pip3 install git+https://github.com/abenassi/Google-Search-API'
        os.system(bashCommand)
        bashCommand = 'sudo apt-get install antiword abiword unrtf poppler-utils libjpeg-dev pstotext'
        os.system(bashCommand)
        bashCommand = 'pip3 install -r requirements.txt'
        os.system(bashCommand)
        bashCommand = 'pip3 install --user -U -r requirements.txt'
        os.system(bashCommand)
    if choice == '0':
        bashCommand = 'clear'
        os.system(bashCommand)
        exit()
    
start_time = time.time()
bashCommand = 'clear'
os.system(bashCommand)
exit_p = 0
bashCommand = 'printf "\e[8;50;100t"'
os.system(bashCommand)
while exit_p == 0:
	menu(start_time)
