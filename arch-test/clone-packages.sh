#!/bin/bash

mkdir -p "pkgs" && cd "pkgs"
while read -r line; do
    git clone "https://gitlab.archlinux.org/archlinux/packaging/packages/$line.git"
done <../packages.csv
