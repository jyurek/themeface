#!/usr/bin/env bash

curl -s https://thoughtbot.com/boston | grep "person-photo" | perl -ne 'print "$_\n" for (/src="(.*?)"/g)' | grep -v no-photo-ralph | cut -d '?' -f 1
