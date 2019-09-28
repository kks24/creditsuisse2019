import logging
import json

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)

@app.route('/lottery', methods=['GET'])
def evaluate3():
    result = [i for i in range(100)]
    logging.info("My result :{}".format(result))
    return jsonify(result);