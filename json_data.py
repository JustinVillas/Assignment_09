import json

personal_info = '''
{
    "Basic_Info": [
        {
            "Name": "Justin Lawrence DL. Villas",
            "Age": "18",
            "Phone": "09123456789",
            "Email": "justinlawrencedlvillas@gmail.com",
            "Birthay": "March 11,2003",
            "Address": "1045 La Avenida St, Mountain View, Estados Unidos",
            "Civil Status": "Single",
            "Hobbies": "Reading Manga, Cycling, Watching Anime"
        }
    ],
    "Education_Atainment":[
        {
            "Elementary": "Elementary Coding School",
            "Junior High School": "Junior Coding High School",
            "Senior High School": "Senior Coding High School",
            "Tertiary": "Tertiary Coding High School"
        }
    ],
    "Skills":[
        {
            "one": "Proficient in using Microsoft Office.",
            "two": "Basic knowledge in Phyton Programming.",
            "three": "Proficient in installation of Cable Cignal.",
            "four": "Proficient in video editing using vllo and filmora."
        }
    ],
    "Profile": [
        {
            "=": "An independent and responsible individual who is up to challenges." 
        }
    ]
}
'''

data = json.loads(personal_info)
# the json file where the output must be stored
out_file = open("resume.json", "w")

json.dump(data, out_file, indent=4)

out_file.close()
