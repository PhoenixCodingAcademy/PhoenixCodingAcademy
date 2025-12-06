'''
From the command line, run:
  flask --app main.py --debug run
This will start the Flask web but watch it for changes and automatically reload the site.
'''
import glob
import os
import sys
import yaml
import random
from flask import Flask, Blueprint, render_template, request, send_file, redirect, send_from_directory, jsonify


get_name = Blueprint('get_name', __name__)

@get_name.route('/api/name', methods=['GET'])
def getName():
  return jsonify({ 'results': { 'name': 'rob'}})


@get_name.route('/api/random', methods=['GET'])
def getRandom():
  n = int(request.args['n'] or 10)
  r = random.Random()
  return jsonify([r.randint(0,1000000000) for x in range(n)])


@get_name.route('/api/models', methods=['GET'])
def getModels():
  from huggingface_hub import list_models
  count = int(request.args.get('count', 50))
  skip = int(request.args.get('skip', 0))
  
  models = list_models(filter="llm", limit=None)
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

  return jsonify(result)
  