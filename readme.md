# Alexa PySSML

This is a sample Alexa skill that uses the PySSML project https://github.com/sumsted/pyssml.

PySSML is inspired and based on JavaScript project https://github.com/mandnyc/ssml-builder.

## Usage

1. You'll need a couple of modules. bottle to run app and requests to run tests

2. You'll need to pip install pyssml

2. Create a yaml file that contains the following or replace host and port in app.py

    ```
    PROJECT:
        HOST: 0.0.0.0
        PORT: 8086
    ```

3. Run app.py and send requests to endpoint /alexa/event.Återm