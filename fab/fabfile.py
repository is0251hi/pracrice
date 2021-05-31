from fabric.api import local

def curl():
    local('curl gaagle.co/api')

def echo():
    a=1
    local_args = locals()
    local(f'echo {local_args}')

