#!/bin/bash

if [[ $1 ]]; then
    url=$1
else
    url="http://web.lasactf.com:14339/entrance.svg"
fi
while :; do
    response=$(curl -s $url)
    if [[ ${#response} == 0 ]]; then
        echo "Unable to fetch anything..."
        exit
    fi
    inkscape -z -e qr.png <(echo $response)
    contents=$(zbarimg qr.png)
    if ! echo $contents | grep "lasactf{" > /dev/null; then
        url=$(echo $contents | sed "s/QR-Code://g")
        echo "Going to $url"
    else
        echo "Got the flag!"
        echo $contents
        break
    fi
done

# your flag is: 'lasactf{a_maze_of_twisty_little_passages}'
