# Use the official SurrealDB image from Docker Hub
FROM surrealdb/surrealdb:latest

# set `src/CryptHub-Platform/components/CryptDB/data` as the working directory
WORKDIR /data

# Expose the port that SurrealDB will run on
EXPOSE ${SURREAL_DB_PORT}

# Set environment variables for the SurrealDB user and password
ENV SURREAL_DB_USER=${SURREAL_DB_USER}
ENV SURREAL_DB_PASSWORD=${SURREAL_DB_PASSWORD}

# Start SurrealDB with the specified user and password
CMD ["start", "--user", "${SURREAL_DB_USER}", "--pass", "${SURREAL_DB_PASSWORD}", "file:/data/${SURREAL_DB_NAME}.db"]
