#!/bin/sh
LIST_OF_APPS = "mariadb-server python python-pip default-libmysqlclient-dev"
LIST_OF_PYTHON = "MySQL-python mysql-connector"

apt install -y $LIST_OF_APPS
apt install -y $LIST_OF_PYTHON