#!/bin/sh

# Run this script at the root directory where your pdf files are.

# $1 : the path of a PDF file
countpdfpages()
{
    return `pdftk $1 dump_data output | grep -i NumberOfPages | cut -d ' ' -f2`
}

document=`find . -maxdepth 2  -name "*.pdf"`
acc=0
for i in $document
do
	echo $i
	countpdfpages $i
	pages=$?
	acc=$(($acc+$pages))
done

echo $acc
