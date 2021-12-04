# Generates an OAuth access token.
source ../.env
curl -d client_id=$TWITCH_CLIENT_ID \
     -d client_secret=$TWITCH_CLIENT_SECRET \
     -d grant_type=client_credentials "https://id.twitch.tv/oauth2/token" -s | jq '.'