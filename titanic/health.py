from flask import Flask, request, jsonify


def ok():
    """
    This function responds to a request for /healthy

    """
    
    result =  {
        "status": "alive"
        ""
    }

    return jsonify(result)