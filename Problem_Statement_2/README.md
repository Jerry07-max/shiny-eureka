**Problem Statement 2**
 - The automated test scripts are for the following questions:
   2a) **System Health Monitoring Script**:
        Develop a script that monitors the health of a Linux system.
        It should check CPU usage, memory usage, disk space, and running processes.
        If any of these metrics exceed predefined thresholds (e.g., CPU usage > 80%), the script should send an alert to the console or a log file.

   2b) **Log File Analyzer**:
        Create a script that analyzes web server logs (e.g., Apache, Nginx) for common patterns such as the number of 404 errors, the most requested pages, or IP addresses with the most requests.
        The script should output a summarized report.

 - For 2a) Ensure the following library is installed by running the code in Windows Powershell:

          pip install psutil

 - Run the python script by running the following code in Powershell:

         python <script_name>.py

 - For 2b) Ensure the 'access.log' file is available in the directory where the test script is located.

 - Run the python script by running the following code in Powershell:

         python <script_name>.py
  
  
   
