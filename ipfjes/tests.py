"""
Unittests for ipfjes
"""
from opal.core.test import OpalTestCase

from ipfjes import models, patient_lists

class WeHaveSomeModelsTestCase(OpalTestCase):
    def test_there_is_a_model(self):
        demographics = models.Demographics(name='Larry')
        self.assertEqual('Larry', demographics.name)

class PatientListTestCase(OpalTestCase):
    def test_queryset(self):
        all_patients = patient_lists.AllPatientsList()
        self.assertEqual(0, all_patients.get_queryset().count())
        patient, episode = self.new_patient_and_episode_please()
        self.assertEqual(1, all_patients.get_queryset().count())