#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    def __init__(self, name ="Some Person", job ="Some Job"):
        self.name = name
        self.job = job

    def get_name(self):
        print("Getting name")
        return self._name
    
    def get_job(self):
        print("Getting job")
        return self._job
    
    def set_name(self, name):
        if (name in str (len(name)>=1 and len(name) <=25 )):
            print(f"{name.title()}")
            self._name = name
        else:
            print("Name must be string between 1 and 25 characters.")

    def set_job(self, job):
        if job in self.APPROVED_JOBS:
            self._job = job
        else:
            print("Job must be in list of approved jobs.")

    name = property(get_name, set_name)
    job = property(get_job, set_job)

