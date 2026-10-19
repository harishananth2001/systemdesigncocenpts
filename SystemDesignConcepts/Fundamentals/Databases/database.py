# Django ORM example
appointments = Appointment.objects.select_related(
    "patient", "doctor"
).all()
