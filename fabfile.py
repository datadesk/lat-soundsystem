from fabric.api import env, cd, run, sudo


env.hosts = ("raspberrypi.local",)
env.user = "pi"
env.known_hosts = ''
env.remote_interrupt = True


def pull():
    with cd("/home/pi/Code/lat-soundsystem/repo"):
        run("git pull origin master")


def restartapache():
    sudo("service apache2 restart")


def updateservice():
    with cd("/home/pi/Code/lat-soundsystem/repo"):
        sudo("cp listener.service /etc/systemd/system/dweet.service")
    sudo("systemctl start dweet.service")


def stopservice():
    sudo("systemctl stop dweet.service")


def servicestatus():
    sudo("systemctl status dweet.service")


def deploy():
    pull()
    restartapache()
    updateservice()