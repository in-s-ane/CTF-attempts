#!/bin/bash

set -e

url="http://web.lasactf.com:14339/entrance.svg"
while :; do
    response=$(curl -s $url -m 5)
    if [[ ${#response} == 0 ]]; then
        echo "Unable to fetch anything..."
        return
    fi
    inkscape -z -e qr.png <(echo $response)
    contents=$(zbarimg qr.png)
    if ! echo $contents | grep "lasactf{" > /dev/null; then
        url=$contents
        echo $url
    else
        echo "Got the flag!"
        echo $contents
    fi
done
