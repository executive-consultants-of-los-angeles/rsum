#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from home.schema.cv import CV
from home.schema.section import Section
from home.schema.subsection import SubSection
from home.schema.project import Project
from home.schema.projectitem import ProjectItem
from home.schema.entryitem import EntryItem
from home.schema.entry import Entry

import home
import yaml

home.CV = CV()
home.Section = Section()
home.SubSection = SubSection()
home.Project = Project()
home.ProjectItem = ProjectItem()
home.EntryItem = EntryItem()
home.Entry = Entry()

class CVTestCase(TestCase):
    def setUp(self):
        f = open('/srv/rsum/cvs/abridged.yml')
        self.abridged = yaml.load(f.read())
        f.close()
        f = open('/srv/rsum/cvs/complete.yml')
        self.complete = yaml.load(f.read())
        f.close

    def test_save_abridged_cv(self):
        abridged = self.abridged
        cv = CV()
        result = cv.save_cv(abridged, 'abridged', template='acecv')

        self.assertEqual(result.name, 'abridged')
        self.assertEqual(result.template, 'acecv')

    def test_save_complete_cv(self):
        complete = self.complete
        cv = CV()
        result = cv.save_cv(complete, 'complete', template='acecv')
    
        self.assertEqual(result.name, 'complete')
        self.assertEqual(result.template, 'acecv')


class SectionTestCase(TestCase):
    def setUp(self):
        f = open('/srv/rsum/cvs/abridged.yml')
        self.abridged = yaml.load(f.read())
        f.close()

    def test_save_section(self):
        abridged = self.abridged
        cv = CV()
        cv.name = 'abridged'
        cv.template = 'acecv'
        cv.save()

        for name, section in sorted(
            abridged.items(),
            key=lambda t: t[1].get('id')
        ):
            section_instance = Section()
            section_result = section_instance.save_section(
                cv,
                section,
                name
            )
            self.assertEqual(
                list(Section.objects.values()),
                list(section_result)
            )


class SubSectionTestCase(TestCase):
    def setUp(self):
        f = open('/srv/rsum/cvs/abridged.yml')
        self.abridged = yaml.load(f.read())
        f.close()

    def test_save_sub_section(self):
        abridged = self.abridged
        cv = CV()
        cv.name = 'abridged'
        cv.save()

        for name, section in sorted(
            abridged.items(),
            key=lambda t: t[1].get('id')
        ):
            if isinstance(section, str):
                pass
            else:
                s = Section()
                s.cv = cv
                s.name = name
                s.content = type(section)
                s.save()
                ss = SubSection()
                ss_result = ss.save_sub_sections(section, s)
                for item in ss_result:
                    try:
                        self.assertEqual(
                            list(Project.objects.values()),
                            list(item)
                        ) 
                    except:
                        self.assertEqual(
                            None,
                            item 
                        ) 
