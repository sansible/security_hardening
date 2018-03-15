import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_cron(host):
    at_allow = host.file('/etc/at.allow')
    assert at_allow.exists
    assert at_allow.user == 'root'
    assert at_allow.group == 'root'
    assert at_allow.mode == 0o644

    cron_allow = host.file('/etc/cron.allow')
    assert cron_allow.exists
    assert cron_allow.user == 'root'
    assert cron_allow.group == 'root'
    assert cron_allow.mode == 0o644

    crontab = host.file('/etc/crontab')
    assert crontab.exists
    assert crontab.user == 'root'
    assert crontab.group == 'root'
    assert crontab.mode == 0o600


def test_grub(host):
    grub_cfg = host.file('/boot/grub/grub.cfg')
    assert grub_cfg.exists
    assert grub_cfg.mode == 0o400


def test_root_access(host):
    passwd = host.file('/etc/passwd')
    assert passwd.exists
    assert passwd.contains('root:.*:/usr/sbin/nologin$')

    securetty = host.file('/etc/securetty')
    assert securetty.mode == 0o644


def test_ssh(host):
    sshd_config = host.file('/etc/ssh/sshd_config')
    assert sshd_config.exists
    assert sshd_config.user == 'root'
    assert sshd_config.mode == 0o644


def test_sysctl(host):
    assert host.sysctl('net.ipv4.conf.all.accept_redirects') == 0
    assert host.sysctl('net.ipv4.conf.all.accept_source_route') == 0
    assert host.sysctl('net.ipv4.conf.all.send_redirects') == 0
    assert host.sysctl('net.ipv6.conf.all.accept_source_route') == 0

    # The following are unreliable in docker and have been commented out
    # assert host.sysctl('fs.suid_dumpable') == 0
    # assert host.sysctl('net.ipv4.conf.all.secure_redirects') == 0
    # assert host.sysctl('net.ipv6.conf.all.accept_redirects') == 0


def test_ubuntu_dir(host):
    home_ubuntu = host.file('/home/ubuntu')
    assert home_ubuntu.exists
    assert home_ubuntu.mode == 0o750


def test_user_limits(host):
    limits_conf = host.file('/etc/security/limits.conf')
    assert limits_conf.exists
    assert limits_conf.contains('*                hard    core            0')
