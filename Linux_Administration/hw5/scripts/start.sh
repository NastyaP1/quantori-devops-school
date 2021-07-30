#!/bin/bash

declare -ir SUCCESS=0
declare -ir FAILURE=1

isAppRunning() {
  /filesharing/bin/status.sh >/dev/null 2>&1
  return $?
}

if ! isAppRunning ; then
  nohup python3 -m http.server $1 >/dev/null 2>&1 &
  if ! isAppRunning ; then
    exit ${FAILURE}
  fi
fi
