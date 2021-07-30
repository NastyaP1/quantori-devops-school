## Описание

Написать systemV init script и systemd service unit для filesharing service. В качестве транспорта для передачи файлов использовать протокол http. Номер tcp порта и папку для раздачи файлов можно вынести в файл с параметрами, можно оставить в скрипте, на ваше усмотрение (предлагаю 8080 и /opt/share). В качестве web сервера предлагаю использовать python -m http.server (или python -m SimpleHTTPServer для python2).
Продемонстрировать работоспособность: start, stop, restart, status.

## Результат

### Реализация init script

Для управления сервисом были созданы filesharing(init), start.sh, stop.sh, status.sh скрипты, которые можно найти здесь: [scripts](https://github.com/NastyaP1/quantori-devops-school/blob/master/Linux_Administration/hw5/scripts)

Листинг /etc/init.d/filesharing:

```
#!/bin/bash

export PORT=8080

stop() {
	echo -n "Shutting down python http service"
 	echo
    source /filesharing/bin/stop.sh
}
status() {
	echo -n "Status of the python http service:"
    echo
	source /filesharing/bin/status.sh
}
restart() {
	echo -n "Restarting python http service"
	echo
    source /filesharing/bin/stop.sh

	source /filesharing/bin/start.sh $PORT
}
start() {
    echo -n "Starting python http service"
    echo
    source /filesharing/bin/start.sh $PORT
}

case "$1" in
	start)
	    start
	;;
	stop)
        stop
	;;
	status)
		status
	;;
	restart)
		restart
	;;
	*)
		echo "Usage: python http service {start|stop|status|restart}"
		exit 1
	;;
esac

```

**Демонстрация**

Для демонстрации использовались следующие команды:

```
/etc/init.d/filesharing status

/etc/init.d/filesharing start

/etc/init.d/filesharing stop

/etc/init.d/filesharing restart

wget http://0.0.0.0:8080/opt/share/file

```

![](https://github.com/NastyaP1/quantori-devops-school/blob/master/Linux_Administration/hw5/resources/LinuxAdm1.png)

![](https://github.com/NastyaP1/quantori-devops-school/blob/master/Linux_Administration/hw5/resources/LinuxAdm2.png)

![](https://github.com/NastyaP1/quantori-devops-school/blob/master/Linux_Administration/hw5/resources/LinuxAdm3.png)



### Реализация service script

Для управления сервисом были созданы filesharing.service, start_service.sh скрипты, которые можно найти здесь: [scripts](https://github.com/NastyaP1/quantori-devops-school/blob/master/Linux_Administration/hw5/scripts)

Листинг /etc/systemd/system/filesharing.service:

```
[Unit]
Description=Python http filesharing service

[Service]
Environment=HTTP_PORT=8080

ExecStart=/filesharing/bin/start_service.sh

```

Для демонстрации использовались следующие команды:

```
sudo systemctl start filesharing

sudo systemctl status filesharing

sudo systemctl restart filesharing

sudo systemctl stop filesharing

wget http://0.0.0.0:8080/opt/share/file

```

![](https://github.com/NastyaP1/quantori-devops-school/blob/master/Linux_Administration/hw5/resources/LinuxAdm4.png)
