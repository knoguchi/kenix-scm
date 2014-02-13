import os
import sys

from fabric.api import env, local, task

HERE = os.path.dirname(os.path.abspath(__file__))
SERVER = os.path.join(HERE, 'server')
CLIENT = os.path.join(HERE, 'client')
sys.path.append(HERE)

@task
def link_dev(client='client', server='server'):
    """
    ln -s client/build server/static
    """

    def replace_link(src, target):
        src = os.path.abspath(os.path.join(client, src))
        target = os.path.abspath(os.path.join(server, target))
        if os.path.exists(target):
            print "target exists"
            if not os.path.islink(target):
                print >> sys.stderr, 'Refusing to replace {} - not a link'.format(target)
                return
            os.remove(target)

        print 'ln -s {} {}'.format(src, target)
        os.symlink(src, target)

    replace_link('build', 'static')

@task
def unlink(server='server'):
    """
    rm server/static
    """

    def unlink(target):
        target = os.path.abspath(os.path.join(server, target))
        print "removing", target
        os.remove(target)
    unlink('static')


@task
def serve():
    datastore_path = os.path.join(HERE, 'data')
    port = 9090
    admin_port = 9000

    server_params = ("--host=127.0.0.1 --storage_path=%s --port=%i --admin_port=%i" % (datastore_path, port, admin_port))
    dev_server = 'dev_appserver.py'
    pipeline = '2>&1 | cc.sh'

    cmd = "%s %s %s %s" % (dev_server, server_params, SERVER, pipeline)
    local(cmd, capture=False)
    
