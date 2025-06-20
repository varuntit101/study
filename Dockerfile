# ---- Builder Stage ----
# Use a full Python image to build our dependencies
FROM python:3.11-slim AS builder

WORKDIR /usr/src/app

# Install build dependencies
RUN pip install --upgrade pip
# Copy only the requirements file to leverage Docker layer caching
COPY requirements.txt ./
# Install dependencies into a specific directory
RUN pip wheel --no-cache-dir --wheel-dir /usr/src/app/wheels -r requirements.txt


# ---- Final Stage ----
# Use a smaller, more secure base image for the final container
FROM python:3.11-slim

# Create a non-root user for security
RUN useradd --create-home appuser
WORKDIR /home/appuser

# Copy dependencies from the builder stage
COPY --from=builder /usr/src/app/wheels /wheels
COPY --from=builder /usr/src/app/requirements.txt .

# Install the dependencies from the local wheel files
RUN pip install --no-cache /wheels/*

# Copy the application code
COPY app.py .

# Switch to the non-root user
USER appuser

# Command to run the application
CMD ["python", "app.py"]
