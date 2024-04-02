
from flask import Flask, request, render_template

app = Flask(__name__)

# Mapping of FBI Codes  to crime types
crime_types = {
    "6": "THEFT",
    "08B": "BATTERY",
    "18": "NARCOTICS",
    "14": "CRIMINAL DAMAGE",
    "26": "OTHER OFFENSE",
    "11": "DECEPTIVE PRACTICE",
    "08A": "ASSAULT",
    "3": "ROBBERY",
    "7": "MOTOR VEHICLE THEFT",
    "5": "BURGLARY",
    "04B": "BATTERY",
    "04A": "ASSAULT",
    "15": "WEAPONS VIOLATION",
    "20": "OFFENSE INVOLVING CHILDREN",
    "2": "CRIM SEXUAL ASSAULT",
    "24": "PUBLIC PEACE VIOLATION",
    "10": "DECEPTIVE PRACTICE",
    "17": "SEX OFFENSE",
    "01A": "HOMICIDE",
    "16": "PROSTITUTION",
    "22": "LIQUOR LAW VIOLATION",
    "9": "ARSON",
    "19": "GAMBLING",
    "13": "INTIMIDATION"
}

@app.route('/')
def index():
    return render_template('index.html', primary_type="", error="")

@app.route('/predict_crime_type', methods=['POST'])
def predict_crime_type():
    iucr = request.form.get('iucr')
    arrest = request.form.get('arrest')
    domestic = request.form.get('domestic')
    beat = request.form.get('beat')
    district = request.form.get('district')
    fbi_code = request.form.get('fbi_code')
    year = request.form.get('year')

    primary_type = None
    if fbi_code:
        primary_type = crime_types.get(fbi_code)
    elif arrest:
        primary_type = crime_types.get(arrest)
    elif domestic:
        primary_type = crime_types.get(domestic)
    elif beat:
        primary_type = crime_types.get(beat)
    elif iucr:
        primary_type = crime_types.get(iucr)
    elif district:
        primary_type = crime_types.get(district)
    elif year:
        primary_type = crime_types.get(year)

    if primary_type:
        return render_template('index.html', primary_type=primary_type, error="")
    else:
        return render_template('index.html', primary_type="", error="Primary type not found for the given input")

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5000,debug=True)
