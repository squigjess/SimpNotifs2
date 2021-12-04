# Subscribes to a stream.online event
source ../.env
curl -H "Authorization: Bearer $TWITCH_OAUTH_ACCESS_TOKEN" \
     -H "Client-ID: $TWITCH_CLIENT_ID" \
     -H "Content-Type: application/json" \
     -d "{ \
          \"version\": \"1\", \
          \"type\": \"stream.online\", \
          \"condition\": {\"broadcaster_user_id\": \"12826\"}, \
          \"transport\": { \
               \"method\": \"webhook\", \
               \"callback\": \"https://example.com/webhooks/callback\", \
               \"secret\": \"abcdefghij0123456789\" \
          }  \
     }" "https://localhost:8008/hello" -s | jq '.'
