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
    echo "OAuth Token: "
    read api_key
    echo "OAuth Token Secret: "
    read api_secret
    echo "Spoonacular API key: "
    read spoonacular_api_key
    printf "export CONSUMER_API_KEY=\'$consumer_key\'\nexport CONSUMER_SECRET_KEY=\'$consumer_secret\'\nexport APP_SECRET=\'$api_key\'\nexport APP_KEY=\'$api_secret\'\nexport SPOONACULAR_API_KEY=\'$spoonacular_api_key\'\n" > .env
fi

echo "Done!"
