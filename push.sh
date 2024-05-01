#!/bin/bash

while Line= read -r line; do
    eval "$line"
done < push.txt