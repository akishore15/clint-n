#!/bin/bash
sudo apt install git
git clone https://github.com/akishore15/clint-n.git --p 85
echo "GIT CLONED, MAPPED AT localhost:85"
echo "CONTINUE [Y / N]"
read ans1
if [ $ans1 -eq "Y" ]
then
echo "OK!"
else
echo "Abort."
portmap=ls --p 85
export portmap
echo "$portmap"
echo "Do you still want to delete this info? [Y / N]"
read confirmans1
if [ $confirmans1 -eq "Y" ]
then
echo "Deleting data permanently..."
sudo kill -9 $(sudo lsof -t -i:85)
else
echo "OK. BOOTING PORT 85..."
google-chrome localhost:85

