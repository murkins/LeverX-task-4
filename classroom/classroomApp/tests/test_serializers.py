from django.test import TestCase

from classroomApp.serializers import *


class PersonaSerializerTestCase(TestCase):
    def test_ok(self):
        user_1 = User.objects.create(username='Kati')
        user_2 = User.objects.create(username='Mary')

        persona_1 = Persona.objects.get(id=1)
        persona_2 = Persona.objects.get(id=2)

        persona_1.name = 'Kate'
        persona_1.is_teacher = False
        persona_1.save()

        persona_2.name = 'Mary'
        persona_2.is_teacher = False
        persona_2.save()

        data = PersonaSerializer([persona_1, persona_2], many=True).data
        expected_data = [
            {
                'id': persona_1.id,
                'user': 'Kati',
                'name': 'Kate',
                'is_teacher': False
            },
            {
                'id': persona_2.id,
                'user': 'Mary',
                'name': 'Mary',
                'is_teacher': False
            },
        ]
        self.assertEqual(expected_data, data)

