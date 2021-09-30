#!/bin/bash

URL = $1

if [[ -z "$URL"]] then ;
    read -p "Enter an url"
    exit
fi


