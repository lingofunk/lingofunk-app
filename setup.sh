#!/usr/bin/env bash
# sync the prerequisite files
function sync() {
    local -n files=$1
    for file in "${files[@]}"; do
        mkdir -p $(dirname $file)
        [ -f ../$file ] && cp -n ../$file $file
    done
}

WEIGHTS=lingofunk-classify-sentiment/lingofunk_classify_sentiment/assets/model/hnatt/weights.h5
EMBEDDING=lingofunk-classify-sentiment/lingofunk_classify_sentiment/assets/embedding/glove.840B.300d.txt

paths=($WEIGHTS $EMBEDDING)

sync paths

# sync the submodules
git submodule update --recursive --remote --init
git pull
