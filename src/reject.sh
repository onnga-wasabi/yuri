#!/bin/zsh
while read line
do
    line=cropped/fc/$line.png
    rm $line
done < ./notYuriTakami.txt
