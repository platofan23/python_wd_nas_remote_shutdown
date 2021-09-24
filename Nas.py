import paramiko
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
client.load_system_host_keys()
client.connect('IP', 22, 'sshd','password' )
stdin, stdout, stderr = client.exec_command('echo -e \'#!/bin/bash\nsleep $((3600*$1 + 60*$2 + $3))\n/usr/sbin/shutdown.sh\'  > ssh.sh')
for line in stdout:
    print('... ' + line.strip('\n'))
stdin, stdout, stderr = client.exec_command('sh ssh.sh seconds minutes hours >> /dev/null 2>&1')
for line in stdout:
    print('... ' + line.strip('\n'))
stdin, stdout, stderr = client.exec_command('killall sshd >> /dev/null 2>&1')
for line in stdout:
    print('... ' + line.strip('\n'))
client.close()
