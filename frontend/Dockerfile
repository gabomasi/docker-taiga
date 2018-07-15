FROM nginx:1.13-alpine

LABEL taiga_version="tag:3.1.3-stable"

ENV TAIGA_VERSION 3.1.3-stable

COPY nginx/ /etc/nginx/conf.d/
# Entrypoint
COPY scripts/ /scripts/
# Frontend compiled code
ADD https://github.com/taigaio/taiga-front-dist/archive/${TAIGA_VERSION}.tar.gz /taiga_frontend/
WORKDIR /taiga_frontend
RUN tar -xzf ${TAIGA_VERSION}.tar.gz -C ./ taiga-front-dist-${TAIGA_VERSION}/dist --strip-components=2 \
    && rm ${TAIGA_VERSION}.tar.gz \
    && chown -R nginx /taiga_frontend \
    && chown -R nginx /scripts/ \
    && chmod +x /scripts/entrypoint.sh \
    && wget https://github.com/taigaio/taiga-contrib-gitlab-auth/archive/3.1.1.tar.gz \
    && tar -xzvf 3.1.1.tar.gz \
    && mkdir plugins \
    && mv taiga-contrib-gitlab-auth-3.1.1/front/dist plugins/gitlab-auth \
    && rm -R taiga-contrib-gitlab-auth-3.1.1 3.1.1.tar.gz

ENTRYPOINT ["/scripts/entrypoint.sh"]
CMD ["nginx", "-g", "daemon off;"]
