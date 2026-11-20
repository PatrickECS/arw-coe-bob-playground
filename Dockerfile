FROM httpd:2.4-alpine

# Copy webpage content into the Apache document root
COPY index.html /usr/local/apache2/htdocs/index.html

# Expose port 80 for HTTP traffic
EXPOSE 80

# Apache runs in the foreground by default in the httpd image
CMD ["httpd-foreground"]