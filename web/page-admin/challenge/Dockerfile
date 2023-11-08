FROM nginx:stable-bullseye

COPY src/* /usr/share/nginx/html/
COPY nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 10005

CMD ["nginx", "-g", "daemon off;"]