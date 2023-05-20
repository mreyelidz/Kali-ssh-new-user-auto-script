import os
import subprocess

def set_up_ssh():
    # Installing the OpenSSH server
    os.system("sudo apt-get -y install openssh-server")

    # Enabling the SSH service at boot time
    os.system("sudo systemctl enable ssh")

    # Starting the SSH service
    os.system("sudo systemctl start ssh")

    # Configuring the firewall to allow SSH traffic
    os.system("sudo ufw allow ssh")

    # Displaying message with instructions after successful setup
    print("\nSSH has been set up successfully!")
    print("Make sure to use your Kali Linux system's IP address while connecting from remote devices.")
    print("You can find the IP address by running the 'ip addr show' command in the terminal.")


def make_new_sudoer():
    # Getting username and password from user input
    new_username = input("Enter the new username: ")
    new_password = input("Enter the new password: ")

    # Adding new user
    add_user_command = f"sudo useradd -m {new_username}"
    subprocess.call(add_user_command.split())

    # Setting password for the new user
    set_password_command = f"sudo passwd {new_username}"
    subprocess.call(set_password_command.split(), input=new_password.encode())

    # Adding the new user to the sudo group
    add_to_sudo_command = f"sudo usermod -aG sudo {new_username}"
    subprocess.call(add_to_sudo_command.split())

    # Display success message
    print(f"User {new_username} has been added and can now use 'sudo' command.")


def main():
    choice = int(input("Enter your choice (1 for SSH setup, 2 for New Sudoer): "))

    if choice == 1:
        set_up_ssh()
    elif choice == 2:
        make_new_sudoer()
    else:
        print("Invalid choice. Please enter either 1 or 2.")

if __name__ == '__main__':
    main()
