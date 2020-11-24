action=$1
if [ $# -lt 1 ]
then
    echo "sh $0 <action>"
    exit
fi
if [ "$action" = "run" ]
then
    python3 manage.py runserver 0.0.0.0:8089 --settings=config.settings.dev
elif [ "$action" = "reset" ]
then
    find ./ -name "00*py*"|xargs rm
    sleep 10
    python3 manage.py makemigrations
    python3 manage.py migrate
elif [ "$action" = "test" ]
then
    # coverage erase
    coverage run  manage.py $* --keepdb
    # coverage report
else
    python3 manage.py $*
fi
