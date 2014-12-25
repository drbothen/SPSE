import subprocess

subprocess.call(['ps','aux'])
subprocess.call(['ls','-al'])



lines = subprocess.check_output(['ls','-al'])

linesplit = lines.split("\n")



handle = subprocess.Popen("ls", stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, close_fds=True)

handle.stdout.read()