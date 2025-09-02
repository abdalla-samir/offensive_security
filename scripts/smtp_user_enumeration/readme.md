# SMTP User Enumeration Script

## Command
```
./smtp_user_enumeration <IP> <usernames.txt>

Ex. ./smtp_user_enumeration 192.168.1.6 usernames.txt
```

## Description
- This is a python script which establishes a connection with SMTP server using `socket`, and perform user enumeration using a file of usernames.
- It pings the IP first to check if the host is up or down.
- If the ip is up, it reads the file and store each username in a list.
- For each user, it establishes a connection and send the following command to the SMTP server: `VRFY <username>`.
- it then prints the result, indicating whether the user exists on the server or not.
- If the IP is down, it gives the following error message: `Ping Failed: Provide a valid ip address`
