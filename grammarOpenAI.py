# -*- coding: utf-8 -*-
"""Untitled15.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1tCy0xrxyD-hd3OWBdU-kQuRPZWfEgjDx
"""

!pip install openai

import os
import openai

def gpt3(stext):
  openai.api_key = "API-Key"
  response = openai.Completion.create(
  model="text-davinci-002",
  prompt=stext,
  temperature=0,
  max_tokens=60,
  top_p=1.0,
  frequency_penalty=0.0,
  presence_penalty=0.0
  )
  content = response.choices[0].text.split('.')
  print(content)
  return response.choices[0].text

query = input()
response = gpt3(query)
print(response)