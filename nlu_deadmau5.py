# simply pulled all examples from here https://www.ibm.com/watson/developercloud/natural-language-understanding/api/v1/#post-analyze together with tweaks

from __future__ import print_function
import json
from watson_developer_cloud import NaturalLanguageUnderstandingV1
from watson_developer_cloud.natural_language_understanding_v1 import Features, EntitiesOptions, KeywordsOptions, CategoriesOptions, ConceptsOptions, EmotionOptions, MetadataOptions, RelationsOptions, SemanticRolesOptions, SentimentOptions


print("\n ENTITIES & KEYWORDS")
natural_language_understanding = NaturalLanguageUnderstandingV1(
    version='2017-02-27',
    username='####',
    password='####')

response = natural_language_understanding.analyze(
    text='Bruce Banner is the Hulk and Bruce Wayne is BATMAN! '
         'Superman fears not Banner, but Wayne.',
    features=Features(entities=EntitiesOptions(), keywords=KeywordsOptions()))

print(json.dumps(response, indent=2))




print("\n CATEGORIES")
response = natural_language_understanding.analyze(
  url='www.ibm.com',
  features=Features(
    categories=CategoriesOptions()))

print(json.dumps(response, indent=2))


print("\n EMOTION SENTIMENT BY ENTITY")
response = natural_language_understanding.analyze(
  text='IBM is an American multinational technology company '
       'headquartered in Armonk, New York, United States, '
       'with operations in over 170 countries.',
  features=Features(
    entities=EntitiesOptions(
      emotion=True,
      sentiment=True,
      limit=2),
    keywords=KeywordsOptions(
      emotion=True,
      sentiment=True,
      limit=2)))

print(json.dumps(response, indent=2))



print("\n CONCEPTS")
response = natural_language_understanding.analyze(
  #url='www.ibm.com',
  url='https://dreamtolearn.com/ryan/r_journey_to_watson',
  features=Features(
    concepts=ConceptsOptions(
      limit=20)))

print(json.dumps(response, indent=2))



print("\n ENTITY DOCUMENT LEVEL SENTIMENT")

response = natural_language_understanding.analyze(
  url='www.cnn.com',
  features=Features(
    entities=EntitiesOptions(
      sentiment=True,
      limit=1)))

print(json.dumps(response, indent=2))


print("\n TARGETED SENTIMENT")
response = natural_language_understanding.analyze(
  url='www.wsj.com/news/markets',
  features=Features(
    sentiment=SentimentOptions(
      targets=['stocks'])))

print(json.dumps(response, indent=2))



print("\n TARGETED EMOTION")
response = natural_language_understanding.analyze(
  html=" \
    <html> \
      <head><title>Fruits</title></head> \
      <body> \
        <h1>Apples and Oranges</h1> \
        <p>I love apples! I don't like oranges.</p> \
      </body> \
    </html>",
  features=Features(
    emotion=EmotionOptions(
      targets=['apples','oranges'])))

print(json.dumps(response, indent=2))


print("\n METADATA")
response = natural_language_understanding.analyze(
  url='www.ibm.com',
  features=Features(
    metadata=MetadataOptions()))

print(json.dumps(response, indent=2))



print("\n RELATIONS")
response = natural_language_understanding.analyze(
  text='Leonardo DiCaprio won Best Actor in a Leading Role \
        for his performance.',
  features=Features(
    relations=RelationsOptions()))

print(json.dumps(response, indent=2))


print("\n SEMANTIC ROLES")
response = natural_language_understanding.analyze(
  text='IBM has one of the largest workforces in the world',
  features=Features(
    semantic_roles=SemanticRolesOptions()))

print(json.dumps(response, indent=2))
