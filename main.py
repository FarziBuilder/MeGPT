import json
from functions import get_video_id_from_url, get_video_transcript, educationChecker,finalReport, learningOutcomes, YTgenerator

with open('watch-history.json', 'r') as file:
    data = json.load(file)

target_date = '2023-05-06'

totalLearnings = ""

#print(YTgenerator("https://www.youtube.com/watch?v=EVMmDNXgpj4"))


for item in data:
  if target_date in item['time']:
      break
  if "not" not in educationChecker(item["title"]) and "Not" not in educationChecker(item["title"]):
    print('\n')
    print(item["title"])
    transcript = get_video_transcript(item["titleUrl"].replace("\u003d", "="))
    #do GPT call for getting the learning outcomes
    try:
      outcomes = learningOutcomes(transcript)
    except Exception as e:
      print("An error occurred while calling learningOutcomes(transcript):", e)
      outcomes = learningOutcomes(item["title"])

    totalLearnings += "\n" + outcomes #correct for 0 later
    print(outcomes)
    print(" ")


#do GPT Call for getting the final Report
print('\n')
print(finalReport(totalLearnings))
    
