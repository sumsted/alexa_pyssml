from bottle import run
from settings import Settings

settings = Settings()
import alexa_api

if __name__ == '__main__':
    run(host=settings.PROJECT['HOST'], port=settings.PROJECT['PORT'], debug=True)
