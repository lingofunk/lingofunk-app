#!/usr/bin/env bash
# sync the prerequisite files
function sync() {
    local -n files=$1
    echo "Copying files..."
    for file in "${files[@]}"; do
        mkdir -p $(dirname $file)
        [ -f ../$file ] && cp -n ../$file $file
    done

    echo "Copying directories..."
    local -n dirs=$2
    for dir in "${dirs[@]}"; do
        [ -d $dir.old ] && rm -r $dir.old
        mv $dir $dir.old
        [ -d ../$dir ] && cp -r ../$dir $dir
    done
}

EMBEDDING=lingofunk-classify-sentiment/lingofunk_classify_sentiment/assets/embedding/glove.840B.300d.txt
MODEL_DIR=lingofunk-classify-sentiment/lingofunk_classify_sentiment/assets/model/hnatt

paths=(
    $EMBEDDING
)

dirpaths=(
    $MODEL_DIR
)

sync paths dirpaths

# sync the submodules
git submodule update --recursive --remote --init
git pull

# lingofunk-classify-sentiment

./lingofunk-transfer-style/download_model.sh
