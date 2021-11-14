# Python-FastAPI
FastAPI is a Python framework and set of tools that enables developers to use a REST interface to call commonly used functions to implement applications. 
It is accessed through a REST API to call common building blocks for an app

Requirements:

    Python 3.6 or higher.

FastAPI stands on the shoulders of giants:

    Starlette for the web parts.
    Pydantic for the data parts.

Installation:

    pip install fastapi.
    
An ASGI server is needed, for production such as Uvicorn or Hypercorn.

    pip install "uvicorn[standard]".
    
Run it on the server with:

    uvicorn main:app --reload.
