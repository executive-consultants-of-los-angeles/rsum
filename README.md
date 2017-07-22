Curiculum Vitae
===============

[![Build Status](https://travis-ci.org/executive-consultants-of-los-angeles/rsum.svg?branch=master)](https://travis-ci.org/executive-consultants-of-los-angeles/rsum)

The point of this is to demonstrate for potential clients that this company is not completely lacking competence.  A truncated version in yaml is below.

```yaml
---
name: "Edward Harris"
  position: "Cloud Architect and / or Software Engineer"
  summary: "Straight shooter with upper management written all over me."
skills: 
  infrastructure_automation:
    ansible: "4 years"
  system_administration:
    bash: "15 years"
    vim: "15 years"
  cloud_architecture: 
    amazon_web_services: "9 years" 
    microsoft_azure: "1 year"
    google_cloud: "1 year"
    digital_ocean: "4 years"
  software_development: 
    agile: "4 years"
    sdlc: "15 years" 
    scm: "10 years"
    git: "4 years"
    svn: "2 years"
  linux_unix:
    redhat: "15 years"
    debian: "13 years"
  programming:
    python: "4 years" 
    java: "1 year"
    php: "15 years"
  relational_databases:
    postgresql: "10 years"
    mysql: "15 years"
experience:
  company: "Undisclosed Client"
    duration: "6 months"
    location: "Los Angeles, California"
    position: "Cloud Architect and Software Engineer"
    projects:
      jupyterhub:
        - "Automated deployment via Ansible."
        - "Instructed analysts on programming Python."
      ansible_tower:
        - "Refactored code to increase stability and security."
        - "Upgraded Ansible Tower more than once."
        - "Added logging with New Relic and Splunk to Tower."
      continuous_integration:
        - "Was handed a project that was a year late."
        - "Also running a stack I was unfamiliar with."
        - "In less than a quarter I got the team of 6 devs to deliver on time."
        - "Enabled continous delivery and automated testing of new features."
  company: "Undisclosed Client"
    duration: "9 months"
    location: "Los Angeles, California"
    position: "Lead Python Developer / Cloud Architect / Build Manager"
    projects:
      lead_python_developer:
        - "Wrote and enforced a reasonable Python style guide."
        - "Designed and coded a web scraping tool to collect client information."
        - "Ran daily scrum meetings with other developers."
      build_manager:
        - "Deployed Atlassian JIRA and Bitbucket services to client owned hardware."
        - "Provided instruction on git and gitflow to a team of more than 20 developers."
        - "Implemented continous delivery and automated testing with Jenkins and Ansible."
      cloud_architect:
        - "Responsible for automation of client infrastructure with Ansible."
        - "Reduced deployment time for key resources from weeks to hours."
        - "Managed Amazon Web Services budget for client project."
  company: "Undisclosed Client"
    duration: "1 year"
    location: "Oakland, California"
    position: "Chief Technical Officer"
    projects:
      webmaster:
        - "Ran all of the company's websites."
        - "Mostly written in PHP, sadly."      
      systems_administrator:
        - "Responsible for monitoring, backups, and database maintenance."
        - "Used HAProxy for High Availability applications."
        - "Automated infrastructure tasks with Ansible."
...
# vim: ft=ansible:
```

Requirements
------------

A willingness to learn.
```bash
ansible-galaxy install executive-consultants-of-los-angeles.r-sum-
```

Role Variables
--------------

None yet.

Dependencies
------------

None.

Example Playbook
----------------

```yaml
- hosts: all 
  roles:
     - { 
          role: executive-consultants-of-los-angeles.r-sum-,
          what_is_six_times_seven: 42 
        }
```

License
-------

GPLv3

Author Information
------------------

Written by Edward Harris for ECLA.
