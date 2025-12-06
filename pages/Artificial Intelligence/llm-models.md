<title>LLM Models</title>


[Hugging Face](https://huggingface.co/) is the de facto central repository for LLMs, with ~638,000 models tagged as LLMs (filterable by tasks like text-generation). It includes open-source models from Meta, Mistral, EleutherAI, and more.

To search the models in the web browser: https://huggingface.co/models?other=LLM

Python code to get the models:
```python
  from huggingface_hub import list_models
  count = int(request.args.get('count', 100))
  token = request.args.get('token', None)

  models = list_models(filter="llm", limit=count, token=token)
  result = []
  for model in models:
    result.append({
                    'id': model.id,
                    'private': model.private,
                    'downloads': getattr(model, 'downloads', 0),
                    'likes': model.likes or 0,
                    'private': model.private,
                    'tags': model.pipeline_tag,
                    'library_name': model.library_name,
                    'trending_score': model.trending_score,
                    'created_at': model.created_at.isoformat() if model.created_at else None
                  })
```

Sample: [THIS PAGE](/llm-models)