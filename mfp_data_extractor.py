import myfitnesspal
import datetime
import csv

client = myfitnesspal.Client('choppermanster', password='')

start = datetime.datetime.strptime("19-03-2020", "%d-%m-%Y")
end = datetime.datetime.today()
date_generated = [start + datetime.timedelta(days=x) for x in range((end-start).days)]

with open('MFP_data.csv', mode='w') as MFP_data:
    writer = csv.writer(MFP_data)
    for date in date_generated:
        meals = client.get_date(date.year, date.month, date.day).meals
        for meal in meals: # 6 meals: bfast, lunch, dinner, morning snack, midday snack, post-dinner
            for entry in meal:
                nut_info = entry.nutrition_information
                if "," in entry.name:
                    writer.writerow([date, meal.name, '"' + entry.name + '"', entry.quantity, entry.unit, nut_info['calories'], nut_info['carbohydrates'], nut_info['fat'], nut_info['protein'], nut_info['sodium'], nut_info['sugar']])
                else:
                    writer.writerow([date, meal.name, entry.name, entry.quantity, entry.unit, nut_info['calories'], nut_info['carbohydrates'], nut_info['fat'], nut_info['protein'], nut_info['sodium'], nut_info['sugar']])
