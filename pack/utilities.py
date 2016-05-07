import os


def execute_shell_command(shell_command):
    os.system(shell_command)

# command = "hotspot -c hotspot.config -f ev6.flp -p my.ptrace -o my.ttrace -steady_file my.steady -model_type grid \ -grid_layer_file my.lcf"
# execute_shell_command(command)
