#!/bin/bash

function usage()
{
   cat << HEREDOC

   Usage: $progname -u <username> -g <admin_group> -d <ftp_dir>

   optional arguments:
     -h                            show this help message and exit
     -u   username                 username account
     -g   admin_group              name of admin group
     -d   ftp_dir                  ftp-server directory

HEREDOC
}

if [ "$USER" = "root" ]
then

    HOME_DIR="/home"
    USER_ACCOUNT=''
    ADMIN_GROUP="ftp_admin"
    PASSWD=''
    FTP_DIR="/var/ftp"

    while getopts u:g:d:h opt
    do
        case $opt in
            u)
                USER_ACCOUNT=${OPTARG}
            ;;
            g)
                ADMIN_GROUP=${OPTARG}
            ;;
            d)
                FTP_DIR=${OPTARG}
            ;;
            h)
                usage
                exit 0
            ;;
            *)
                echo "ERROR: Unrecognised Option $opt"
                usage
                exit 1
            ;;
        esac
    done

    if [ -z $USER_ACCOUNT ];
    then
        echo "Not all mandatory options are set!"
        usage
        exit 1
    fi

    NOW=$(date +"%Y-%m-%d-%X")
    LOGFILE="log-$NOW.log"

    cut -d: -f1 /etc/passwd | grep "$USER_ACCOUNT" > /dev/null
    if [ $? -eq 0 ];then
        echo "ERROR: User account: $USER_ACCOUNT already exists."
        echo "ERROR: User account: $USER_ACCOUNT already exists." >> "$LOGFILE"
    else
        /usr/sbin/useradd -d "$HOME_DIR/$USER_ACCOUNT" "$USER_ACCOUNT"
        PASSWD=$(pwgen 10 1)
        echo "$USER_ACCOUNT:$PASSWD" | chpasswd
        echo "$USER_ACCOUNT $PASSWD" >> "$LOGFILE"
        echo "The user $USER_ACCOUNT has been created and has the password: $PASSWD"
        mkdir $FTP_DIR/$USER_ACCOUNT
        echo "Directory $FTP_DIR/$USER_ACCOUNT has been created" >> "$LOGFILE"
        echo "Directory $FTP_DIR/$USER_ACCOUNT has been created"
        sudo chown -R $USER_ACCOUNT:$ADMIN_GROUP $FTP_DIR/$USER_ACCOUNT
      fi
   exit 0
else
   echo "ERROR: You must be a root user to execute this script."
   exit 1
fi
