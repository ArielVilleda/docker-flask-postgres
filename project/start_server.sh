if [ "$FLASK_ENV" == "test" ] || [ "$FLASK_ENV" == "dev" ];
then
    echo "NOT DEPLOYED ENVIROMENT. Access to the container and use <flask run -h 0 -p 5000> instead"
    echo "Keeping container alive..."
    while true; do sleep 1; done
else
    echo "Starting gunicorn server for PRODUCTION ENVIROMENT" 
    gunicorn --bind 0:5000 --workers 2 app:main
fi