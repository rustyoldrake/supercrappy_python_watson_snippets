import json
from watson_developer_cloud import NaturalLanguageUnderstandingV1
import watson_developer_cloud.natural_language_understanding.features.v1 as \
    features

# you need to go to bluemix - https://console.ng.bluemix.net/ sign up for free, and then stand up a free Watson NLU endpoint to get your own keys
natural_language_understanding = NaturalLanguageUnderstandingV1(
    version='2017-02-27',
    username='b26d50dd-xxxx-xxxx-xxxx-c965f958b228',
    password='xxxxxxxxxxx')


response = natural_language_understanding.analyze(
    text='Bruce Banner is the Hulk and Bruce Wayne is BATMAN! '
         'Superman fears not Banner, but Wayne.',
    features=[features.Entities(), features.Keywords()])

print(json.dumps(response, indent=2))
