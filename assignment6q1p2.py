import json

indian_states = {
    "Madhya pradesh": "Bhopal",
    "Karnataka": "Banglore",
    "Maharastra": "Mumbai",
    "West Bengal": "Kolkata",
    "Tamil Nadu": "Chennai",
    "Rajasthan": "Jaipur",
    "Uttarakhand": "Dehradun",
}
with open(r"indian_states.json", "w") as file:
    json.dump(indian_states, file)
with open(r"indian_states.json", "r") as file:
    data = file.readlines()
    print(data)