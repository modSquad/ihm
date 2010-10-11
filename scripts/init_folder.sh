#!/bin/sh

if [ $# -ne 1 ]
then
    echo "Usage : $0 name_of_dir_to_be_created"
    exit
fi

init_arch()
{
    mkdir src
    mkdir src/img
    cp Makefile ../$1
    
    sed "s/XXX/$1/g" Makefile >  
}

dir_name=$1
mkdir $dir_name
cd $dir_name

