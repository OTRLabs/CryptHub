# Use the official SurrealDB image from Docker Hub
FROM surrealdb/surrealdb:latest

# set `src/CryptHub-Platform/components/CryptDB/data` as the working directory
WORKDIR /data

# Expose the port that SurrealDB will run on
EXPOSE 8000

# Set environment variables for the SurrealDB user and password
ENV DB_USER=root
ENV DB_PASSWORD=root

# Start SurrealDB with the specified user and password
CMD ["start", "--user", "root", "--pass", "root", "file:/data/crypthub.db"]
