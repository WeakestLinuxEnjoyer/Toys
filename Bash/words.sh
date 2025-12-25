!# /usr/bin/bash 

# extract unique words from a file
cat man.txt | tr " " "\n" | sort -u
