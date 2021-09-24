<h1> python_wd_nas_remote_shutdown </h1>

<h2>Description of the project</h2>
This is programm to shut down a WD MyCloud EX2 Ultra remotly<br>
The ssh-Server needs to be activated.

<h2>Project status</h2>
The project itself is complete and ready for use. I am open for improvments.

<h2>Requirements</h2>
Requirements for running the webui are:
- python (3.x.x) <br>
- pip (v3) or any other packetmanager <br>
- paramiko

<h2>Installation</h2>
1. Download and Install Python. <br>
For windows go to (https://www.python.org/downloads/) <br>
For linux use <code> sudo apt-get install python3.x </code> <br>
2. Download and install pip-packetmanager <br>
3. Install paramiko <br>
For Windows <code> py -3 -m pip install paramiko </code> <br>
For Linux <code> pip3 install paramiko </code> <br>
4. Now run the NAS.py - File
For Windows <code> py -3 NAS.py </code> <br>
For Linux <code> python3 NAS.py </code> <br>
5. Activate the ssh-Server on your WD MyCloud EX2 Ultra-NAS

<h2>Additional notes:</h2>
- In the python-script enter the IP-Adress for IP, the password for password and the number of hours, minutes and seconds to wait for hours, minutes and seconds. <br>
- When used with cron-jobs it can shutdown the nas at set time
