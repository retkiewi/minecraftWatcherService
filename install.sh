#!/bin/bash
cp ./mcServerWatcher.service /etc/systemd/system/mcServerWatcher.service
systemctl daemon-reload
systemctl restart mcServerWatcher.service
