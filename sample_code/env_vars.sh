#! /usr/bin/env bash

# create a file name variable
file_name=${1}

# create a multi-line text variable and export it
export SALES_DATA=$(cat ${file_name})
echo
echo "SALES_DATA: ${SALES_DATA}"
echo

# create a simple one line variable
export TOKEN_VALUE="WErfar35303"
echo
echo "TOKEN_VALUE: ${TOKEN_VALUE}"
echo
