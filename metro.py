import json
from datetime import datetime

repair_stantion = []

with open("metro.json", "r", encoding="windows-1251") as metro:
    reader = json.load(metro)
    for stantion in reader:
        if stantion["RepairOfEscalators"] != []:
            for repair in stantion["RepairOfEscalators"]:
                dash_in_date = stantion["RepairOfEscalators"][-1]["RepairOfEscalators"].find("-")
                date_end_repair = stantion["RepairOfEscalators"][-1]["RepairOfEscalators"][:dash_in_date]
                date_end_repair_dt = datetime.strptime(date_end_repair, '%d.%m.%Y')
                
                if date_end_repair_dt > datetime.today():
                     repair_stantion.append(stantion["Name"])
print('На сегодняшний день ремеонт эксколатора'
      ' производится на следующих станциях: ', ', '.join(repair_stantion))