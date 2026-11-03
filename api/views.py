from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import View
# Create your views here.
class about(View):
    def get(self,request):
        data = {
            'id':'6',
            'Full_name':'Adhish Santhosh',
            'title':'Software Engineer',
            'bio':'Btech graduate with experience in software development.',
            'email':'adhishsanthosh377@example.com',
            'mobile_number':'+91 7736083294',
            'linkedin_profile':'https://www.linkedin.com/in/adhish-santhosh-3b837935a/',
            'github_profile':'https://github.com/Adhish-Santhosh',
        }
        return JsonResponse(data)
class education(View):
    def get(self,request):
        data={
            'id':'6',
            'institution':'CAPE',
            'university':'APJ abdul kalam technological university',
            'location':"alappuzha",
            'qualification':'B-tech',
            'Start-year':'2022',
            'End-year':'2026',
            'CGPA':'6.32',
            'description':'B-tech computer science student'
        }
        return JsonResponse(data)
class Projects(View):
    def get(Self,request):
        data=[
            
            {
                'id': 1,
                'title': 'Python-MySQL-CRUD-Gym-Database-Management',
                'short description': 'A Python and MySQL-based application designed to manage gym members, trainers, subscriptions, and billing using CRUD operations.',
                'long description': 'The Python-MySQL CRUD Gym Database Management System is a desktop application designed to simplify daily gym operations. It manages member registrations, trainer assignments, subscription details, and billing records using Python and a MySQL relational database.',
                'technologies used': ["Python", "MySQL", "Streamlit"],
                'live url': 'live/',
                'github url': 'https://github.com/Adhish-Santhosh/Python-MySQL-CRUD-Gym-Database-Management',
                'image url': 'image/',
                'featured': 'True'
            },

            {
                'id': 2,
                'title': 'IoT-Environmental-Monitoring-System',
                'short description': 'An IoT-based system that monitors temperature, humidity, air quality, and AQI using sensors and machine learning.',
                'long description': 'The IoT Environmental Monitoring System collects environmental data using ESP8266 and sensors such as LM35, DHT11, and MQ135. The system uses Flask and a machine learning model to analyze environmental conditions and predict air quality levels.',
                'technologies used': ["Python", "Flask", "IoT", "ESP8266", "Machine Learning"],
                'live url': 'live/',
                'github url': 'https://github.com/Adhish-Santhosh/IoT-Environmental-Monitoring-System',
                'image url': 'image/',
                'featured': 'True'
            },

            {
                'id': 3,
                'title': 'Advanced-Image-to-Text-Converter',
                'short description': 'A web application that extracts text from uploaded images and provides additional translation and user interface features.',
                'long description': 'The Advanced Image to Text Converter is a web application that uses image processing and OCR techniques to extract text from images. It provides multiple image uploads, text extraction, translation options, dark mode, and a responsive user interface.',
                'technologies used': ["HTML", "CSS", "JavaScript", "OCR"],
                'live url': 'live/',
                'github url': 'https://github.com/Adhish-Santhosh/Advanced-Image-to-Text-Converter',
                'image url': 'image/',
                'featured': 'True'
            },
        ]
        return JsonResponse(data,safe=False)
class skills(View):
    def get(self,request):
        data = [

            {
                'id': 1,
                'title': 'Python',
                'description': 'Programming, application development, automation, and problem solving.',
                'technologies': ['Python', 'OOP', 'File Handling', 'Exception Handling'],
                'image_url': 'image/python.png',
                'featured': True
            },

            {
                'id': 2,
                'title': 'Django',
                'description': 'Building web applications and REST APIs using the Django framework.',
                'technologies': ['Django', 'REST API', 'JSON', 'URL Routing'],
                'image_url': 'image/django.png',
                'featured': True
            },
            {
                'id': 3,
                'title': 'Web Development',
                'description': 'Creating responsive and interactive websites and web applications.',
                'technologies': ['HTML', 'CSS', 'JavaScript', 'Bootstrap'],
                'image_url': 'image/web-development.png',
                'featured': True
            },

]
        return JsonResponse(data,safe=False)
from django.http import JsonResponse
from django.views.generic import View


class certification(View):

    def get(self, request):

        data = [
            {
                'id': '1',
                'certification_name': 'Python Programming & Web Designing Intern',
                'company': 'CodeDesign Technologies Pvt. Ltd.',
                'duration': '1 month',
                'description': 'Strengthened core Python programming and scripting fundamentals. Designed and built simple web pages using HTML and CSS.',
                'year': '2024'
            },

            {
                'id': '2',
                'certification_name': 'Web Development',
                'company': 'CodeDesign Technologies Pvt. Ltd.',
                'duration': '1 month',
                'description': 'Developed responsive web pages using HTML, CSS and JavaScript.',
                'year': '2024'
            },

            {
                'id':'3',
                'certificate name':'Frontend Application Development Intern',
                'company':'NeST Digital Academy',
                'duration':'1 months',
                'description':'Developed reusable frontend components using Angular, HTML, CSS, and TypeScript.',
                'year':'2025'

            }
        ]

        return JsonResponse(data, safe=False)
