from fabric.api import env, run
import fabric

NEW_PASSWORD = 'NEWSTRONGPASSWORD'

fabric.state.output['running'] = False
fabric.state.output['stdout'] = False

env.use_shell = False
env.user = 'Administrator'
env.password = 'STRONGPASSWORD'
env.skip_bad_hosts = True
env.hosts = [
    'chassis01.example.net',
    'chassis02.example.net',
    'chassis03.example.net',
]

def batch_chpw():
    chassis_str = env.host_string[0:env.host_string.find('.example.net')]

    print "%s" % env.host_string

    # Set Chassis Password
    result = run("set password %s" % NEW_PASSWORD)
    if result:
        print "--Administrator password set."

    print "\n"

    return True
