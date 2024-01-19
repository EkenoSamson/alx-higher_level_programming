## Command line for the win

The task is to play [The CMD challenge](https://cmdchallenge.com/) game that challenges the player on Bash skills. Everything is done via the command line and the questions are becoming increasingly complicated. It’s a good training to improve your command line skills!

## File Transfer Using SFTP

Follow these steps to use the SFTP command-line tool and transfer files to the sandbox environment:

1. **Open Terminal or Command Prompt:**
   - On your local machine, open a terminal or command prompt.

2. **Connect to the Sandbox Environment:**
   - Use the SFTP command to establish a connection to the sandbox environment.
     ```bash
     sftp username@hostname
     ```
   - Replace `username` with your provided username and `hostname` with the provided hostname.
   - Enter the password when prompted.

3. **Navigate to the Target Directory:**
   - Once connected, navigate to the directory in the sandbox environment where you want to upload the screenshots.
     ```bash
     cd /path/to/target/directory
     ```

4. **Upload Screenshots:**
   - Use the SFTP `put` command to upload the screenshots from your local machine to the sandbox environment.
     ```bash
     put local/path/to/screenshot.png
     ```
   - Replace `local/path/to/screenshot.png` with the actual path of the screenshot on your local machine.

5. **Confirm Transfer:**
   - Confirm that the screenshots have been successfully transferred by checking the sandbox directory using the SFTP `ls` command.
     ```bash
     ls
     ```

6. **Push to GitHub:**
   - After confirming the successful transfer, proceed to push the screenshots to GitHub as mentioned in the initial requirements.

### Example:

```bash
