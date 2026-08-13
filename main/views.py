from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import redirect, render


def home(request):
    context = {
        "profile": {
            "name": "Adrian Immanuel Egbuna",
            "title": "Full-Stack Web & Mobile Developer",
            "summary": (
                "Software engineering student and full-stack web and"
                "mobile developer building Django-powered backends,"
                " modern web applications, and cross-platform mobile"
                " apps with React Native. "
                "Passionate about creating practical, database-driven"
                " products with a strong focus on usability, performance, and reliable execution."
            ),
            "email": "adrianegbuna@gmail.com",
            "github": "https://github.com/Adrianegbuna",
            "linkedin": "https://linkedin.com/in/adrian-egbuna-5b2695349",
            "location": "Abuja, Nigeria",
        },
        "skills": [
            "Full-Stack Development",
            "Expo",
            "React-Native",
            "Mobile Development",
            "Python",
            "Django",
            "Web Development",
            "Project Management",
        ],
        "experiences": [
            {
                "date": "2025",
                "role": "Software Engineering Bootcamp Participant",
                "company": "Veritas Software Engineering Bootcamp",
                "description": (
                    "Completed practical software engineering training and was selected "
                    "among several project teams to participate in a software exhibition."
                ),
            },
            {
                "date": "2025",
                "role": "Software Exhibition Project Contributor",
                "company": "MedLink",
                "description": (
                    "Worked with a team of software engineers to build a hospital "
                    "management system designed to connect patients with doctors."
                ),
            },
            {
                "date": "2024",
                "role": "Software Development and Documentation Intern",
                "company": "Tagged Technologies Limited",
                "description": (
                    "Supported web design, software development, and technical "
                    "documentation across internal software tasks."
                ),
            },
            {
                "date": "2023",
                "role": "Software Development Intern",
                "company": "Visual Integrated Services",
                "description": (
                    "Completed a three-month internship focused on the foundations of "
                    "web design and practical software development."
                ),
            },
        ],
        "projects": [
            {
                "name": "MedLink",
                "status": "Team Project",
                "role": "Full-Stack Contributor",
                "image": "main/images/MedLink.png",
                "local_image": True,
                "summary": "Hospital management system that helps patients connect with doctors with ease.",
                "impact": "Built as a collaborative software exhibition project with patient and doctor workflows.",
                "tech": ["Python", "Django", "SQLite", "HTML", "CSS"],
                "live": "#",
                "code": "https://github.com/Adrianegbuna/MedLink",
            },
            {
                "name": "Hostel Accommodation System",
                "status": "Academic Project",
                "role": "Full-Stack Developer",
                "image": "https://placehold.co/760x460/081b28/42e8f0?text=Hostel+System",
                "local_image": False,
                "summary": "Web application for helping students select and pay for preferred hostels.",
                "impact": "Created to simplify accommodation selection and payment flow for students.",
                "tech": ["Django", "Python", "SQLite", "Bootstrap"],
                "live": "#",
                "code": "https://github.com/Adrianegbuna/Hostel-Accomodation-Page",
            },
            {
                "name": "Hospital Scheduling System",
                "status": "Academic Project",
                "role": "Full-Stack Developer",
                "image": "main/images/Hospital Scheduling System.png",
                "local_image": True,
                "summary": "Scheduling system where patients can book appointments with doctors.",
                "impact": "Designed around appointment booking, doctor selection, and patient communication.",
                "tech": ["Python", "Django", "SQLite", "JavaScript"],
                "live": "#",
                "code": "https://github.com/Adrianegbuna/Hospital-Schedule-App",
            },
            {
                "name": "MoodTrack",
                "status": "Completed",
                "role": "Full-Stack Developer",
                "image": "main/images/MoodTrack.png",
                "local_image": True,
                "summary": "Website for creating, viewing, editing, and managing user posts"
                " and understanding the sentiment(emotion) behind them.",
                "impact": "Built to enhance user experience and provide insights into the emotional tone of posts.",
                "tech": ["Django", "HTML", "CSS", "SQLite"],
                "live": "#",
                "code": "https://github.com/Adriaegbuna/MoodTrack",
            },
            {
                "name": "Idoma Youth Development Initiative",
                "status": "Project",
                "role": "Full-Stack Developer",
                "image": "main/images/Idoma Project.png",
                "local_image": True,
                "summary": (
                    "Community-focused website for the Idoma Youth Development Initiative, "
                    "presenting its mission, welcome message, culture, projects, news, and events."
                ),
                "impact": (
                    "Created a clear public web presence for youth empowerment, cultural preservation, "
                    "community education, and development advocacy."
                ),
                "tech": ["HTML", "CSS", "JavaScript", "Responsive Design"],
                "live": "#",
                "code": "https://github.com/Adrianegbuna/Idoma-Youth-Development",
            },
            {
                "name": "Resume Matcher",
                "status": "Academic Project",
                "role": "Full-Stack Developer",
                "image": "main/images/Resume Matcher.png",
                "local_image": True,
                "summary": (
                    "AI-powered resume job matching platform that connects recruiters and job seekers "
                    "through intelligent candidate-opportunity matching."
                ),
                "impact": (
                    "Built role-based entry points for recruiters and job seekers with platform stats "
                    "for active jobs, companies, and registered candidates."
                ),
                "tech": ["Python", "Django", "HTML", "CSS", "AI Matching"],
                "live": "#",
                "code": "https://github.com/Adrianegbuna/Resume_Job_Matching",
            },
        ],
        "achievements": [
            {
                "title": "Software Exhibition Selection",
                "source": "Veritas Software Engineering Bootcamp",
                "year": "2025",
            },
            {
                "title": "Certificate of Participation",
                "source": "Software Exhibition Project",
                "year": "2025",
            },
            {
                "title": "Academic Performance Awards",
                "source": "Secondary School Recognition",
                "year": "2022",
            },
            {
                "title": "Humanitarian Campaign Volunteer",
                "source": "Let's Help Humanitarian Foundation",
                "year": "2022",
            },
        ],
        "certifications": [],
    }

    if request.method == "POST":
        name = request.POST.get("name", "").strip()
        email = request.POST.get("email", "").strip()
        message = request.POST.get("message", "").strip()

        if not name or not email or len(message) < 20:
            messages.error(request, "Please complete the form. Messages must be at least 20 characters.")
            return render(request, "main/home.html", context)

        try:
            send_mail(
                subject=f"Portfolio message from {name}",
                message=f"Name: {name}\nEmail: {email}\n\n{message}",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.CONTACT_RECEIVER_EMAIL],
                fail_silently=False,
            )
        except Exception:
            messages.warning(
                request,
                "The form works, but email delivery failed. Check the Gmail app password in settings.",
            )
        else:
            messages.success(request, "Message sent successfully.")

        return redirect("home")

    return render(request, "main/home.html", context)
