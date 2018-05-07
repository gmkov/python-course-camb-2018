#!/bin/bash -e

a=4

echo "Hello is $a"

cat lsjkdslkd >output 2>errors #we've saved the error message and the status

status=$? #store error status

if [ -s error ] #-s true if file exists, from test function, could be: if test -s error 
then
	echo 'The error file is not empty!' >&2 #save standard error in shell
	exit 1
fi


if [ $status -ne 0 ]
then
	echo 'There was an error!' >&2 #take stdout and put it where stderr is 2
	exit 1
fi