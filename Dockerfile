# Use the official Nginx + Python image as the base for our container.
FROM nginx/unit:1.26.1-python3.9

# Copy SSL certificates to the container.
# COPY ./*.pem  /docker-entrypoint.d/

###############################################################################
# Copy config files to the container.
COPY ./nginx/docker-entrypoint.d/* /docker-entrypoint.d/ 

# Copy the web app to the container.
COPY ./webapp /www
###############################################################################

# Copy the dependencies list to the container.
COPY requirements.txt /config/requirements.txt

# Install Python & pip in the container, then:
#     install Python dependencies,
#     Uninstall pip,
#     Clean up unneeded packages, then finally,
#     Remove package lists (???)
RUN apt update && apt install -y python3-pip                                  \
    && pip3 install -r /config/requirements.txt                               \
    && apt remove -y python3-pip                                              \
    && apt autoremove --purge -y                                              \
    && rm -rf /var/lib/apt/lists/* /etc/apt/sources.list.d/*.list

# export UNIT=$(docker run -d -p 8080:8000 unit-webapp)

# export UNIT=$(                                                         \
#       docker run -d                                                      \
#       --mount type=bind,src="$(pwd)/nginx/config/",dst=/docker-entrypoint.d/   \
#       --mount type=bind,src="$(pwd)/nginx/log/unit.log",dst=/var/log/unit.log  \
#       --mount type=bind,src="$(pwd)/nginx/state",dst=/var/lib/unit             \
#       --mount type=bind,src="$(pwd)/webapp",dst=/www                     \
#       -p 8080:8000 unit-webapp                                           \
#   )

# https://unit.nginx.org/howto/certbot/