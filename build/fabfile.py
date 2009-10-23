import os, os.path

config.project = 'zumazoom'

# Targets:

def local_dev():
    "Deployment target: sambulldevbox.local (this is for testing)"
    config.fab_hosts = ['sam-server.local']
    config.target_dir = '/home/sam/'
    config.target = 'local_dev'
    config.restart_apache = False
    config.migrate_db = True


# def preview():
#     "Deployment target: zumazoom.pocketuniverse.ca"
#     config.fab_hosts = ['zumazoom.pocketuniverse.ca']
#     config.target_dir = '/home/sam/projects/'
#     config.target = 'preview'
#     config.restart_apache = True
#     config.migrate_db = True


def live_test():
    "Deployment target: zumazoom.com"
    config.fab_hosts = ['zumazoom.com']
    config.fab_user = 'zumazoomteam'
    config.target_dir = '/home/zumazoomteam/live_test/'
    config.target = 'prod'
    config.restart_apache = False
    config.migrate_db = False


def live():
    "Deployment target: zumazoom.com"
    config.fab_hosts = ['zumazoom.com']
    config.fab_user = 'zumazoomteam'
    config.target_dir = '/home/zumazoomteam/live/'
    config.target = 'prod'
    config.restart_apache = True
    config.migrate_db = True


# Operations:

def build(tree_ish):
    "Build the deployment directory for the branch/tag specified"
    config.tree_ish = tree_ish
    local('rm -rf /var/tmp/%(project)s')
    local('git archive --format=tar --prefix=%(project)s/ %(tree_ish)s site conf/%(target)s'
            '| (cd /var/tmp/ && tar xf -)', fail='abort')
    local('mv /var/tmp/%(project)s/conf/%(target)s/* /var/tmp/%(project)s/conf/')
    local('rmdir /var/tmp/%(project)s/conf/%(target)s')


@requires('fab_hosts', 'target', 'target_dir', provided_by = [local_dev, live_test, live])
def deploy(tag=None, branch='master'):
    "Build the project and deploy it to a specified environment."
    if tag:
        tree_ish = '%s-%s' % (config.project, tag)
    else:
        tree_ish = branch
    invoke((build, (tree_ish,)))
    old_dir = os.getcwd()
    os.chdir('/var/tmp/%s/site' % config.project)
    rsync_project(config.target_dir, exclude=['log', 'site/zumazoom/media/managed'],
            delete=True, extra_opts='-l')
    os.chdir('/var/tmp/%s/conf' % config.project)
    rsync_project(config.target_dir, exclude=['log', 'site/zumazoom/media/managed'],
            delete=True, extra_opts='-l')
    os.chdir(old_dir)
    if config.migrate_db:
        run('export PYTHONPATH="%(target_dir)ssite/lib/:$PYTHONPATH"; python %(target_dir)ssite/zumazoom/manage.py syncdb', shell=True)
        run('export PYTHONPATH="%(target_dir)ssite/lib/:$PYTHONPATH"; python %(target_dir)ssite/zumazoom/manage.py migrate', shell=True)
    if config.restart_apache:
        sudo('/etc/init.d/apache2 restart')
