# originalLineOfMyFile
This program calculates the net lines of your .py file or other file.
Original lines are the amount of file lines - the lines that we put for the beauty of the file and not to confuse the code
For example this code:

    from os import system
    Wi_Fi_name = input("Please Enter name of your Wi_Fi:\n")
    command = "netsh wlan connect %s"
    Error_message = "Wi_Fi isn't connected\nor this Wi_Fi not signin in your system"

    if system ( command % Wi_Fi_name ) == 0:

        if system("ping 172.217.19.4") == 1:
            print(Error_message)
        else:
            print("Connected!")

    else:
        print(Error_message)

>>>
This code has 16 lines. But 5 of the lines are blank
So it has a total of eleven non-empty lines
It was easier to count blank lines for this file. But what about larger files? That's why I made this app.
