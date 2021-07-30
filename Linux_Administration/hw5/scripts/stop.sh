#!/bin/bash

declare -i SUCCESS=0
declare -i FAILURE=1

timeout=10

isAppRunning() {
  /filesharing/bin/status.sh >/dev/null 2>&1
  return $?
}

isAppRunning
if [ $? -eq 2 ]; then
 exit ${SUCCESS}
fi

PID=$(ps -ww -ef | grep http.server | grep python | awk '{ print $2 }' 2> /dev/null)
echo $PID
if  [ ! -z "${PID}" ]; then
    kill ${PID} > /dev/null 2>&1
fi
waitedfor=0

while isAppRunning && [ ${waitedfor} -lt ${timeout} ] ; do
    (( waitedfor+=2))
    sleep 2
done

# Check whether a hard kill is required
if isAppRunning ; then
   PID=$(ps -ww -ef | grep http.server | grep python | awk '{ print $2 }' 2> /dev/null)
   echo $PID
   if [ ! -z "${PID}" ]; then
       kill -9 ${PID} > /dev/null 2>&1
   else
      echo "ERROR: Python http sefvice could not exit gracefully"
      exit ${FAILURE}
   fi
fi
