#!/bin/bash
set -e

psql -U postgres -c "CREATE DATABASE person_list"
psql -U postgres -c "CREATE USER basic PASSWORD 'person_list'"
