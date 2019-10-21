# create your custom drupal image here, based of official drupal
FROM drupal:8.2

RUN apt-get update && apt-get install -y git \
	&& apt-get clean && apt-get autoremove \
	&& rm -rf /var/lib/apt/lists/*

WORKDIR /var/www/html/themes

# download bootstrap drupal project
RUN git clone --branch 8.x-3.20 --single-branch --depth 1 https://git.drupal.org/project/bootstrap.git \
	&& chown -R www-data:www-data bootstrap

WORKDIR /var/www/html

