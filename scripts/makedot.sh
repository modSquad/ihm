#!/bin/sh

for i in `ls *.dot`
do
    basename=`basename $i .dot`
    echo $basename
    dot -Tpdf -o $basename.pdf $i
done
