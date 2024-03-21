import psutil

# Get a list of all running processes
running_processes = psutil.process_iter(['pid', 'name'])

# Filter processes to get only applications
apps = [proc.info for proc in running_processes if proc.info['name'].endswith('.app')]

# Print the list of applications
for app in apps:
    print(app['name'])
