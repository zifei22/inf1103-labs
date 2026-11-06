FROM python:3.11-slim
WORKDIR /usr/src/app
COPY inventory_manager_oop.py .
CMD ["python", "inventory_manager_oop.py"]