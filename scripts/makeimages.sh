#!/bin/sh

for i in `ls *.dot`
do
    basename=`basename $i .dot`
    echo $basename
    dot -Tsvg -o $basename.svg $i
    convert $basename.svg $basename.png
done
