#!/bin/bash

echo "########################################################################"
echo "##          ##                                                        ##"
echo "##  NOTICE  ##  You may need to run this script with sudo permission  ##"
echo "##          ##                                                        ##"
echo "########################################################################"
echo ""
echo "Press enter to continue ... ( Ctrl-C to abort )"
read > /dev/null

if [ -x "`whereis easy_install`" ]; then
	easy_install requests
elif [ -x "`whereis pip`" ]; then
	pip install requests
else
	echo "What the ....."
	echo "You don't have neither 'easy_install' nor 'pip''"
	echo "Get one from https://pypi.python.org/pypi/setuptools"
	exit 1
fi
