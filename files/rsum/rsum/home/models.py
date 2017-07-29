#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import print_function

import json
import yaml

from django.db import models


# Create your models here.
class CV(models.Model):
    cv_name = models.CharField(max_length=200)

    def check_sections(self):
        cv_i = CV.objects.all()
        if not cv_i.exists():
            cv_f = open('/srv/rsum/cv.yml')
            cv_d = yaml.load(cv_f.read())        
            self.save_cv(cv_d)
            cv_i = CV.objects.all()
            return cv_i
        else:
            return cv_i

    def get_cv(self):
        s = Section()
        cv = {
            'cv_name': 'abridged',
            'sections': s.get_sections(
                CV.objects.filter(
                    id = 1
                )
            ),
        }
        return cv

    def save_cv(self, cv):
        cv_i = CV()
        cv_i.cv_name = 'abridged' 
        cv_i.save()

        for name, section in cv.get('cv').iteritems():
            s = Section()
            s.save_section(cv_i, name, section)

        return CV.objects.values_list() 


class Section(models.Model):
    cv = models.ForeignKey(CV, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, default='section')
    value = models.CharField(max_length=200, null=True) 
    iterable = models.BooleanField(default=False)

    def get_sections(self, cv):
        sections = []
        for section in list(
            Section.objects.filter(
                cv = cv
            ).values()):
            if section.get('value') == u"<type 'list'>":
                ss = SubSection( section = self )  
                section.update({
                    'value': ss.get_sub_section(
                        Section.objects.filter(
                            id = section.get('id')
                        )
                    ),
                })
            if section.get('value') == u"<type 'dict'>":
                ss = SubSection( section = self )  
                section.update({
                    'value': ss.get_sub_section(
                        Section.objects.filter(
                            id = section.get('id')
                        )
                    ),
                })
            sections.append(section)
        return sections
    
    def save_section(self, cv, name, section):
        s_i = Section()
        s_i.cv = cv
        s_i.name = name 
        if type(section) == type(str()):
            s_i.value = section
            s_i.save()
        else:
            s_i.value = type(section)
            s_i.iterable = True
            s_i.save()
            ss = SubSection()
            ss.save_sub_sections(section, s_i)

        return Section.objects.values_list()
    
class SubSection(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    value = models.CharField(max_length=200, null=True)

    def get_sub_section(self, section):
        subsections = []
        for subsection in list(
            SubSection.objects.filter(
                section = section
            ).values() 
        ):
            p = Project() 
            if subsection.get('value') == u"<type 'list'>":
                subsection.update({
                    'value': p.get_projects(
                        SubSection.objects.filter(
                            id = subsection.get('id')
                        )
                    )
                })
            else:
                subsection.update({
                    'value': list(
                        Project.objects.filter(
                            sub_section = subsection.get('id')  
                        ).values()
                    )
                })
            subsections.append(subsection)
        return subsections
                    
    
    def save_sub_sections(self, sub_section, section):
        if type(sub_section) == type(dict()):
            for k, v in sub_section.iteritems():
                ss_i = SubSection()
                ss_i.section = section
                ss_i.value = type(sub_section)
                ss_i.name = k
                ss_i.save()
                p = Project() 
                p.save_project_dict(v, ss_i)
        elif type(sub_section) == type(list()):
            for c,i in enumerate(sub_section):
                ss_i = SubSection()
                ss_i.section = section
                ss_i.value = type(sub_section)
                ss_i.name = str(c) 
                ss_i.save()
                p = Project()
                p.save_project_list(i, ss_i)
        return SubSection.objects.values()

class Project(models.Model):
    sub_section = models.ForeignKey(SubSection, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    value = models.CharField(max_length=200, null=True)

    def get_projects(self, subsection):
        projects = []
        for project in list(
            Project.objects.filter(
                sub_section = subsection
            ).values()
        ):
            pli = ProjectItems()
            project.update({
                'value': pli.get_project_items(
                    Project.objects.filter(
                        id = project.get('id')
                    )
                ) 
            })
            projects.append(project) 
        return projects

    def save_project_dict(self, projects, sub_section):
        for k, v in projects.iteritems():
            p_i = Project()
            p_i.sub_section = sub_section
            p_i.name = k 
            p_i.value = v
            p_i.save()
        return Project.objects.values_list() 

    def save_project_list(self, projects, sub_section):
        for k,v in projects.iteritems():
            p_i = Project()
            p_i.sub_section = sub_section
            p_i.name = k
            p_i.value = type(v)
            p_i.save()
            pi = ProjectItems()
            pi.save_project_items(v, p_i)
        return Project.objects.values_list()

class ProjectItems(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    value = models.CharField(max_length=200, null = True) 
    iterable = models.BooleanField(default=False)

    def get_project_items(self, project):
        project_items = []
        for project_item in list(
            ProjectItems.objects.filter(
                project = project
            ).values()
        ):
            if project_item.get('value') == u"<type 'dict'>":
                pe = ProjectEntry()
                project_item.update({
                    'value': pe.get_entry(
                        ProjectItems.objects.filter(
                            id = project_item.get('id')
                        )
                    )
                })        
                project_items.append(project_item)
            else:
                project_items.append(project_item)
        return project_items

    def save_project_items(self, project_item, project):
        for key,p_entry in project_item.iteritems():
            pi_i = ProjectItems()
            pi_i.project = project
            pi_i.name = key
            if type(p_entry) == type(dict()):
                pi_i.value = type(p_entry)
                pi_i.iterable = True
                pi_i.save()
                pe = ProjectEntry()
                pe.save_entry(p_entry, pi_i)
            else:
                pi_i.value = p_entry
                pi_i.save()
        return ProjectItems.objects.values_list() 


class ProjectEntry(models.Model):
    project_item_list = models.ForeignKey(ProjectItems, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null = True)
    value = models.CharField(max_length=200, null = True) 

    def get_entry(self, project_item):
        entries = []
        for entry in list(
            ProjectEntry.objects.filter(
                project_item_list = project_item
            ).values()
        ):
            eli = EntryListItem()
            entry.update({
                'value': eli.get_list_item(
                    ProjectEntry.objects.filter(
                        id = entry.get('id') 
                    )
                ) 
            })
            entries.append(entry)
        return entries

    def save_entry(self, entry, pi_l):
        for k, v in entry.iteritems():
            pe_i = ProjectEntry()
            pe_i.project_item_list = pi_l
            pe_i.name = k
            pe_i.value = type(v)
            pe_i.save()
            eli = EntryListItem()
            eli.save_list_item(v, pe_i)
        return ProjectEntry.objects.values_list()


class EntryListItem(models.Model):
    project_entry = models.ForeignKey(ProjectEntry, on_delete=models.CASCADE)
    value = models.CharField(max_length=200, null=True)
    
    def get_list_item(self, entry):
        items = []
        for item in list(
            EntryListItem.objects.filter(
                project_entry = entry
            ).values()
        ):
            items.append(item)
        return items
            

    def save_list_item(self, list_item, pe):
        for i in list_item:
            eli = EntryListItem()
            eli.project_entry = pe
            eli.value = i
            eli.save()
        return EntryListItem.objects.values_list() 