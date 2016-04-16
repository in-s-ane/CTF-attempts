#!/bin/bash

# Extract the 5000 frames
# if [[ ! -d render ]]; then
#     mkdir render
# fi

# blender -b ufo.blend -s 1 -e 5000 -o //render -a
# mv render*.png render

# Compare each frame
# if [[ ! -d diffs ]]; then
#     mkdir diffs
# fi

# for frame in $(ls *.png); do
    # for render in $(ls render); do
    #     echo $render
    #     compare $frame render/$render -compose src "diffs/${render}-${frame}-diff.png"
    # done
# done

frame1="263"
frame2="1337"
frame3="3333"
frame4="3999"
frame5="4545"

echo "flag{$frame1,$frame2,$frame3,$frame4,$frame5}"

# We can't just run `diff`, so let's use imagemagick's `compare`.
# Scroll through each diff and note the frames where there is no red
# flag{263,1337,3333,3999,4545}
