declare -ir INSERVICE=0
declare -ir STOPPED=2

PID=$(ps -ww -ef|grep python | grep http.server | awk '{print $2}' 2> /dev/null)

if [ ! -z "${PID}" ]; then
   echo "pid=$PID"
   uptime=`ps -eo etime,pid | grep " $PID" | awk '{print $1}'`
   echo "Process uptime         : $uptime"
   echo
   echo "IN-SERVICE"
   exit ${INSERVICE}
else
   echo "STOPPED"
   exit ${STOPPED}
fi
