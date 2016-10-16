from unittest import TestCase

import requests

class TestIntents(TestCase):
    URL = "http://localhost:8086/alexa/event"

    def test_story(self):
        story_request = {
            "session": {
                "sessionId": "amzn1.echo-api.session.09283094802384",
                "user": {
                    "userId": "amzn1.ask.account.2634876283764"
                },
                "new": False,
                "application": {
                    "applicationId": "amzn1.ask.skill.09283048203"
                }
            },
            "version": "1.0",
            "request": {
                "intent": {
                    "name": "storyIntent"
                },
                "locale": "en-US",
                "requestId": "amzn1.echo-api.request.234234234",
                "type": "IntentRequest",
                "timestamp": "2016-09-25T01:10:47Z"
            },
            "context": {
                "AudioPlayer": {
                    "playerActivity": "IDLE"
                },
                "System": {
                    "application": {
                        "applicationId": "amzn1.ask.skill.234234"
                    },
                    "device": {
                        "supportedInterfaces": {
                            "AudioPlayer": {}
                        }
                    },
                    "user": {
                        "userId": "amzn1.ask.account.234234234"
                    }
                }
            }
        }

        response = requests.post(self.URL, json=story_request)
        print("story: %s" % str(response.json()))
        self.assertTrue('outputSpeech' in response.json()['response'])
        self.assertTrue('card' in response.json()['response'])