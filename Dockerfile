# Extend the official Rasa SDK image
FROM rasa/rasa-sdk:latest
USER root
# Add a custom python library (e.g. jupyter)
RUN pip --no-cache-dir install requests
USER 1001