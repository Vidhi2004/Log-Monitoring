#!/bin/bash

mkdir -p ./logs

# Simulated log entries
echo "INFO: system running" > ./logs/syslog_test.log
echo "WARNING: memory usage high" >> ./logs/syslog_test.log
echo "ERROR: failed to connect to DB" >> ./logs/syslog_test.log
