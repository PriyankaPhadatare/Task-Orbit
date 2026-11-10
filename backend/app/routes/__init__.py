from . import alerts, api_docs, auth, availability, classrooms, health, planner, predict, subjects, tasks, teacher, workload

BLUEPRINTS = [
    health.bp, api_docs.bp, auth.bp, subjects.bp, availability.bp, tasks.bp,
    workload.bp, predict.bp, planner.bp, alerts.bp,
    classrooms.bp, teacher.bp,
]
