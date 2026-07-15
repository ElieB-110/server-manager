import subprocess

if __name__ == "__main__":
    # Transfer settings
    localStorageLocation = "C:\ "
    serverUserName = "elie_b"
    serverStorageLocation = f"/home/{serverUserName}/"
    serverIP = "10.253.109.160" # Should be queried from an external location (work in conjunction with broadcast IP from server)
    remoteLocation = f"{serverUserName}@{serverIP}:{serverStorageLocation}"

    # Menu Navigation
    userSelection = "A"
    loopContinue = True
    uploadAgain = "N"
    make_Changes = "N"

    # Menu Loop
    while loopContinue:
        print("************************************************************************************************************************\nElie's File Manager: Transfer Settings")
        print("************************************************************************************************************************")
        print(f"Local Storage Location: {localStorageLocation}\nServer IP: {serverIP}\nServer User Name: {serverUserName}\nServer Storage Location: {serverStorageLocation}")
        print("************************************************************************************************************************")
        make_Changes = input("\nWould you like to make any changes? (Y/N): ")

        if make_Changes in ["Y","y","N","n"]:
            make_Changes = make_Changes.upper()

            match make_Changes:
                case "Y":
                    subLoopContinue = True
                    while subLoopContinue:
                        print("A) Local Storage Location\nB) Server Storage Location\nC) Server IP Address\nD) Server Username\nX) Exit submenu")
                        changeOption = input("Enter an option: ")
                        
                        while changeOption not in ["a","A","b","B","c","C","d","D","x","X"]:
                            print("Invalid selection. Must be one of: [A,B,C,D,X]")
                            changeOption = input("Enter an option: ")
                        changeOption = changeOption.upper()

                        match changeOption:
                            case "A":
                                oldLocalStorageLocation = localStorageLocation
                                newLocalStorageLocation = input("Enter the new local storage location: ")
                                localStorageLocation = newLocalStorageLocation
                                print(f"Local storage location changed from [{oldLocalStorageLocation}] to [{newLocalStorageLocation}]")

                            case "B":
                                oldServerStorageLocation = serverStorageLocation
                                newServerStorageLocation = input("Enter the new server storage location: ")
                                serverStorageLocation = newServerStorageLocation
                                print(f"Server storage location changed from [{oldServerStorageLocation}] to [{newServerStorageLocation}]")

                            case "C":
                                oldServerIP = serverIP
                                newServerIP = input("Enter the new server IP: ")
                                serverIP = newServerIP
                                print(f"Server IP address changed from [{oldServerIP}] to [{newServerIP}]")

                            case "D":
                                oldServerUserName = serverUserName
                                newServerUserName = input("Enter the new server username: ")
                                serverUserName = newServerUserName
                                print(f"Server username changed from [{oldServerUserName}] to [{newServerUserName}]")
                                
                            case 'X':
                                print("Exiting submenu. Proceeding to connection attempt.")
                                subLoopContinue = False

                        subprocess.run("PAUSE", shell=True)
                        subprocess.run("CLS", shell=True)

                case "N":
                    pass
        else:
            print("Invalid input. Assumed character: N.\nNo changes made. Proceeding...")

        # Minor warning to user.
        print("\nWARNING: Ensure that this machine is on the same network as the server.")
        subprocess.run("pause", shell=True)
        subprocess.run("cls", shell=True)

        # Display sub-menu and receive user input
        print("************************************************************************************************************************\nTransfer Mode")
        print("************************************************************************************************************************")
        print("A) Upload files to server\nB) Download files from server\n************************************************************************************************************************")

        mode_Selection = input("\nSelect an option: ")
        while mode_Selection not in ["a","A","b","B"]:
            print("Invalid input. Selection must be in range: ['a','A','b','B'].")
            mode_Selection = input("Select an option: ")
        mode_Selection = mode_Selection.upper()

        subprocess.run("pause", shell=True)
        subprocess.run("cls", shell=True)

        # Execute upload/download logic. May need to to have a toggle for the -r flag id necessary.
        match mode_Selection:
            case "A":
                print("\n************************************************************************************************************************\nAttempting connection to home-server...")
                upload_process = subprocess.run([
                    "scp",
                    "-r",
                    localStorageLocation,
                    remoteLocation
                ])

                match upload_process.returncode:
                    case 0: # Can delete the files locally if the upload was successful
                        print("\nFile(s) successfully uploaded.\n************************************************************************************************************************")
                        uploadAgain = input("Upload again? (Y/N): ")

                        if uploadAgain in ["Y","y","N","n"]:
                            uploadAgain = uploadAgain.upper()
                            match uploadAgain:
                                case "Y":
                                    pass
                                case "N":
                                    print("Exiting program...")
                                    loopContinue = False
                        else:
                            print("Invalid input. Assumed character: N.\nExiting program...")
                            loopContinue = False

                    case _:
                        print("\nUpload failed!\nEnsure that the server & client are on the same network; and that all settings are valid.\n************************************************************************************************************************")
                        tryAgain = input("\nTry again? (Y/N): ")

                        if tryAgain in ["Y","y","N","n"]:
                            tryAgain = tryAgain.upper()
                            match tryAgain:
                                case "Y":
                                    pass
                                case "N":
                                    print("Exiting program...")
                                    loopContinue = False
                        else:
                            print("Invalid input. Assumed character: N.\nExiting program...")
                            loopContinue = False

            case "B":
                print("\n************************************************************************************************************************\nAttempting connection to home-server...")
                download_process = subprocess.run([
                    "scp",
                    "-r",
                    remoteLocation,
                    localStorageLocation
                ])

                match download_process.returncode:
                    case 0:
                        print("\nVideo(s) successfully downloaded.\n************************************************************************************************************************")
                        downloadAgain = input("Download again? (Y/N): ")

                        if downloadAgain in ["Y","y","N","n"]:
                            downloadAgain = downloadAgain.upper()
                            match downloadAgain:
                                case "Y":
                                    subprocess.run("cls", shell=True)
                                    continue
                                case "N":
                                    print("Exiting program...")
                                    loopContinue = False
                        else:
                            print("Invalid input. Assumed character: N.\nExiting program...")
                            loopContinue = False

                    case _:
                        print("\nDownload failed!\nEnsure that the server & client are on the same network; and that all settings are valid.\n************************************************************************************************************************")
                        tryAgain = input("\nTry again? (Y/N): ")

                        if tryAgain in ["Y","y","N","n"]:
                            tryAgain = tryAgain.upper()
                            match tryAgain:
                                case "Y":
                                    subprocess.run("cls", shell=True)
                                    continue
                                case "N":
                                    print("Exiting program...")
                                    loopContinue = False
                        else:
                            print("Invalid input. Assumed character: N.\nExiting program...")
                            loopContinue = False

        # Neaten up loop iterations       
        subprocess.run("pause", shell=True)
        subprocess.run("cls", shell=True)