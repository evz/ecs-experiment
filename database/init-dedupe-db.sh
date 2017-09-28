#!/bin/bash
set -e

psql -U postgres -c "CREATE DATABASE person_list"
psql -U postgres -c "CREATE USER person_list PASSWORD 'person_list'"
