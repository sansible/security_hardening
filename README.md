# Security Hardening

Master: [![Build Status](https://travis-ci.org/sansible/security_hardening.svg?branch=master)](https://travis-ci.org/sansible/security_hardening)  
Develop: [![Build Status](https://travis-ci.org/sansible/security_hardening.svg?branch=develop)](https://travis-ci.org/sansible/security_hardening)

* [ansible.cfg](#ansible-cfg)
* [Installation and Dependencies](#installation-and-dependencies)
* [Tags](#tags)
* [Examples](#examples)

This roles installs the Security Hardening fixes to make Ubuntu less
vulnerable.

Included fixes:

* Installs latest security updates via aptitude
* SSH root disable and key access only
* Disable ping
* Restrict crons to root only
* Disable core dumps
* Purges old kernels (optional)

**Note** this role installs security hardening updates on each run and is
therefore not idempotent.


## Installation and Dependencies

To install run `ansible-galaxy install sansible.security_hardening` or add this
to your `roles.yml`.

```YAML
- name: sansible.security_hardening
  version: v2.0
```

and run `ansible-galaxy install -p ./roles -r roles.yml`


## Tags

This role uses one tag: **build** 

* `build` - Installs Security Hardening and all its dependencies.


## Examples

To install:

```YAML
- name: Install and configure Security Hardening
  hosts: "somehost"

  roles:
    - role: sansible.security_hardening
      sansible_security_hardening_purge_old_kernels: yes
```
