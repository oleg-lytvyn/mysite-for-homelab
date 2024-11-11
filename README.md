# mysite-for-homelab

### Install packages requirements.txt 
`python3 -m pip install -r requirements.txt`

### Python virtual environment
Install - `python3 -m venv name_env`
Activate - `source name_env/bin/activate`

### Applying initial database migrations
cd ./path
`python3 manage.py migrate`

### Running the development server
`python3 manage.py runserver`
If you take a look at your console, you will see the GET request performed by your browser:

[01/Jan/2024 10:00:15] "GET / HTTP/1.1" 200 16351

You can run the Django development server on a custom host and port or tell Django to load a specific settings file, as follows:

`python3 manage.py runserver 127.0.0.1:8001 --settings=mysite.settings`

## SSH Port Forwarding:
You can use SSH port forwarding to tunnel the traffic from the VM to your local machine. Follow these steps:

On your local machine, establish an SSH connection to the VM with port forwarding:
`ssh -L 8000:localhost:8000 user@vm_ip_address`

## Configure Django to Allow External Access:
Alternatively, you can configure Django to allow external access to the development server. Follow these steps:

Open your project's `settings.py` file on the VM.
Locate the ALLOWED_HOSTS setting and modify it to include the IP address or hostname of your VM:
pythonCopyALLOWED_HOSTS = ['vm_ip_address', 'localhost']
Replace vm_ip_address with the actual IP address or hostname of your VM.
Save the changes to settings.py.
Start the Django development server with the following command:
Copypython3 manage.py runserver 0.0.0.0:8000
This binds the server to all available network interfaces, allowing external access.