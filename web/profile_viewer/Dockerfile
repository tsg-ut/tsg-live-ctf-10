FROM node:18-alpine
WORKDIR /app
COPY --chown=node:node dist/ /app/
RUN chown -R node:node /app
USER node

RUN npm ci --only=production && rm -rf ~/.npm
EXPOSE 3456
ENV FLAG="TSGLIVE{7w1n574r_cyc10n3_run4w4y}"
CMD ["node", "server.js"]
