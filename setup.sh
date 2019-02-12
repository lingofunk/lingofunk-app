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

SENTIMENT_DIR=lingofunk-classify-sentiment/lingofunk_classify_sentiment/assets
SENTIMENT_EMBEDDING=$SENTIMENT_DIR/embedding/glove.840B.300d.txt
SENTIMENT_MODEL_DIR=$SENTIMENT_DIR/model/hnatt

RELEVANCE_DIR=lingofunk-classify-relevance/lingofunk_classify_relevance/assets
RELEVANCE_MODEL_DIR=$SENTIMENT_DIR/model/quora
RELEVANCE_PREPROCESSOR=$SENTIMENT_DIR/model/utils/preprocessor.pkl

paths=(
    $SENTIMENT_EMBEDDING
    $RELEVANCE_PREPROCESSOR
)

dirpaths=(
    $SENTIMENT_MODEL_DIR
    $RELEVANCE_MODEL_DIR
)

sync paths dirpaths

# sync the submodules
git submodule update --recursive --remote --init
git pull

# lingofunk-classify-sentiment

./lingofunk-transfer-style/download_model.sh
