import psutil
import logging
import time

# Setting up logging file to log alerts
logging.basicConfig(filename='system_health.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Defining thresholds for all the alerts
Cpu_Threshold = 80  # 80%
Memory_Threshold = 75  # 75%
Disk_Threshold = 90  # 90%
Running_Processes = 200 #200

# Function checking CPU usage
def check_cpu_usage():
    cpu_usage = psutil.cpu_percent(interval=1)
    if cpu_usage > Cpu_Threshold:
        logging.warning(f"High CPU usage detected: {cpu_usage}%")
        print(f"ALERT: High CPU usage: {cpu_usage}%")

# Function checking memory usage
def check_memory_usage():
    memory = psutil.virtual_memory()
    if memory.percent > Memory_Threshold:
        logging.warning(f"High memory usage detected: {memory.percent}%")
        print(f"ALERT: High memory usage: {memory.percent}%")

# Function checking Disk Usage
def check_disk_usage():
    disk = psutil.disk_usage('/')
    if disk.percent > Disk_Threshold:
        logging.warning(f"Low disk space: {disk.percent}% used")
        print(f"ALERT: Low disk space: {disk.percent}% used")

# Function checking number of running processes
def check_running_processes():
    process_count = len(psutil.pids())
    logging.info(f"Number of running processes: {process_count}")
    print(f"Running processes: {process_count}")
    if process_count > Running_Processes:
       logging.warning(f"More Processes are being run")
       print(f"ALERT: More processes are being run:", process_count) 

# Main function monitoring system health
def monitor_system():
    while True:
        check_cpu_usage()
        check_memory_usage()
        check_disk_usage()
        check_running_processes()
        time.sleep(10)  # Check every 10 seconds

if __name__ == "__main__":
    monitor_system()
