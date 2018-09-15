FROM nginx:1.15-alpine

LABEL taiga_version="tag:3.4.2-stable"

ENV TAIGA_VERSION 3.4.2-stable
ENV TAIGA_GITLAB_AUTH_VERSION 3.1.1

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
    && wget https://github.com/taigaio/taiga-contrib-gitlab-auth/archive/${TAIGA_GITLAB_AUTH_VERSION}.tar.gz \
    && tar -xzvf ${TAIGA_GITLAB_AUTH_VERSION}.tar.gz \
    && mkdir plugins \
    && mv taiga-contrib-gitlab-auth-${TAIGA_GITLAB_AUTH_VERSION}/front/dist plugins/gitlab-auth \
    && rm -R taiga-contrib-gitlab-auth-${TAIGA_GITLAB_AUTH_VERSION} ${TAIGA_GITLAB_AUTH_VERSION}.tar.gz

ENTRYPOINT ["/scripts/entrypoint.sh"]
CMD ["nginx", "-g", "daemon off;"]
