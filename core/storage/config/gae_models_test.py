# coding: utf-8
#
# Copyright 2018 The Oppia Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS-IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Tests for core.storage.config.gae_models."""
from __future__ import absolute_import  # pylint: disable=import-only-modules
from __future__ import unicode_literals  # pylint: disable=import-only-modules

from core.platform import models
from core.tests import test_utils
import feconf

(base_models, config_models) = models.Registry.import_models(
    [models.NAMES.base_model, models.NAMES.config])


class ConfigPropertyModelUnitTests(test_utils.GenericTestBase):
    """Test ConfigPropertyModel class."""

    def test_get_deletion_policy(self):
        self.assertEqual(
            config_models.ConfigPropertyModel.get_deletion_policy(),
            base_models.DELETION_POLICY.NOT_APPLICABLE)

    def test_has_reference_to_user_id(self):
        self.assertStaticMethod(
            config_models.ConfigPropertyModel, 'has_reference_to_user_id')
        self.assertFalse(
            config_models.ConfigPropertyModel.has_reference_to_user_id('id_x'))

    def test_create_model(self):
        config_model = config_models.ConfigPropertyModel(
            value='b')
        self.assertEqual(config_model.value, 'b')

    def test_commit(self):
        config_model1 = config_models.ConfigPropertyModel(
            id='config_model1', value='c')
        config_model1.commit(feconf.SYSTEM_COMMITTER_ID, [])
        retrieved_model1 = config_models.ConfigPropertyModel.get_version(
            'config_model1', 1)
        self.assertEqual(retrieved_model1.value, 'c')
        retrieved_model1.value = 'd'
        retrieved_model1.commit(feconf.SYSTEM_COMMITTER_ID, [])
        retrieved_model2 = config_models.ConfigPropertyModel.get_version(
            'config_model1', 2)
        self.assertEqual(retrieved_model2.value, 'd')
