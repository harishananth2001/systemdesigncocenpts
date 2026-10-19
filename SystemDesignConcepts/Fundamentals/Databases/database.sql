-- Find appointments belonging to patient 1:
SELECT *
FROM appointments
WHERE patient_id = 1;

-- Find appointments with patient and doctor names:
SELECT
    a.id,
    p.name AS patient_name,
    d.name AS doctor_name,
    a.appointment_time
FROM appointments a
JOIN patients p ON a.patient_id = p.id
JOIN doctors d ON a.doctor_id = d.id;

