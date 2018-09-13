from fabric.api import env, cd, run, sudo


env.hosts = ("raspberrypi.local",)
env.user = "pi"
env.known_hosts = ''
env.remote_interrupt = True


def pull():
    with cd("/home/pi/Code/lat-soundsystem/repo"):
        run("git pull origin master")


def restartapache():
    sudo("sudo service apache2 restart")


def deploy():
    pull()
    restartapache()
