#/bin/bash

echo "Setting up Python environment..."

if [ -f ".env" ]
then
    echo ".env present."
else
    echo "Consumer Key: "
    read consumer_key
    echo "Consumer Secret: "
    read consumer_secret
    echo "API Key: "
    read api_key
    echo "API Secret: "
    read api_secret
    printf "export CONSUMER_API_KEY=\'$consumer_key\'\nexport CONSUMER_SECRET_KEY=\'$consumer_secret\'\nexport APP_SECRET=\'$api_key\'\nexport APP_KEY=\'$api_secret\'\n" > .env
    echo "Don't forget to source .env!"
fi

echo "Done!"
