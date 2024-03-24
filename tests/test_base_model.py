from models.base_model import BaseModel
import unittest
from datetime import datetime

class test_base_model(unittest.TestCase):

    def setUp(self):
        self.base_model = BaseModel()

    def test_unique_id(self):
        other_models = BaseModel()
        self.assertNotEqual(self.base_model.id, other_models.id)
    
    def test_string_representation(self):
        expected_str = f"[{self.base_model.__class__.__name__}] ({self.base_model.id}) {self.base_model.__dict__}"
        self.assertEqual(str(self.base_model), expected_str)
    
    def test_timestamps_initialized(self):
        self.assertIsInstance(self.base_model.created_at, datetime)
        self.assertIsInstance(self.base_model.updated_at, datetime)

    
    def test_save_updates_timestamp(self):
        old_updated_at = self.base_model.updated_at
        self.base_model.save()
        self.assertNotEqual(old_updated_at, self.base_model.updated_at)
    def test_to_dict(self):
        obj_dict = self.base_model.to_dict()
        self.assertIsInstance(obj_dict, dict)
        self.assertIn('__class__', obj_dict)
        self.assertIn('created_at', obj_dict)
        self.assertIn('updated_at', obj_dict)
        self.assertEqual(obj_dict['__class__'], self.base_model.__class__.__name__)
        self.assertEqual(obj_dict['created_at'], self.base_model.created_at.isoformat())
        self.assertEqual(obj_dict['updated_at'], self.base_model.updated_at.isoformat())