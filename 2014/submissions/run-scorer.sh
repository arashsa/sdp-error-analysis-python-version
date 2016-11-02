#!/bin/bash

set -e

for team in *; do 
  for track in open closed; do 
    for format in dm pas pcedt; do 
      for file in $team/$track.$format.?.sdp; do 
        if [ -f $file ]; then 
          echo $file; 
          ../toolkit/run.sh Scorer ../test/$format.sdp $file \
            > ${file%%sdp}score 2>&1;
        fi; 
      done; 
    done; 
  done; 
done
