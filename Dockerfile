# Explicit base-image version (do not use python:latest)
FROM python:3.10-slim

# Build-time metadata arguments
ARG BUILD_DATE
ARG VCS_REF
ARG VERSION=1.0.0

# Add OCI labels for image metadata and traceability (Part 23)
LABEL org.opencontainers.image.title="student-ml-api" \
      org.opencontainers.image.description="ML Inference API for Advanced MLOps" \
      org.opencontainers.image.version="${VERSION}" \
      org.opencontainers.image.revision="${VCS_REF}" \
      org.opencontainers.image.created="${BUILD_DATE}" \
      org.opencontainers.image.authors="Muhammad Saad (i230077)"

# Define application working directory
WORKDIR /app

# Dependency installation - optimized layer ordering to leverage Docker cache
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application source code and VERSION after dependency layer
COPY app.py .
COPY VERSION .

# Expose API port
EXPOSE 5000

# Define runtime entrypoint command
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "5000"]
