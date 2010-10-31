#!/bin/sh

for i in `ls *.svg`
do
    basename=`basename $i .svg`
    echo $basename
    inkscape -A  $basename.pdf $basename.svg
done
