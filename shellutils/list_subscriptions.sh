# Lists all events that the application is currently subscribed to.
source ../.env
curl -H "Authorization: Bearer $TWITCH_OAUTH_ACCESS_TOKEN" \
     -H "Client-ID: $TWITCH_CLIENT_ID" "https://api.twitch.tv/helix/eventsub/subscriptions" -s | jq '.'
