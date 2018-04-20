#!/bin/zsh
while read line
do
    line=cropped/$line.png
    rm $line
done < ./notYuriTakami.txt
