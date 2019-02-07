#!/usr/bin/env bash
WEIGHTS=lingofunk-classify-sentiment/lingofunk_classify_sentiment/assets/model/hnatt/weights.h5
EMBEDDING=lingofunk-classify-sentiment/lingofunk_classify_sentiment/assets/embedding/glove.840B.300d.txt
cp ../$WEIGHTS $WEIGHTS
cp ../$EMBEDDING $EMBEDDING
git submodule update --recursive --remote --init
git pull