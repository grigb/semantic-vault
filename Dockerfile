FROM graphiti-debug:latest
RUN pip install frontmatter
RUN pip install huggingface_hub

COPY ./graphiti/server/graph_service /app/graph_service

CMD ["uvicorn", "graph_service.main:app", "--host", "0.0.0.0", "--port", "9083"]
