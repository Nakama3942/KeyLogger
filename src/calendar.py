#  Copyright © 2022 Kalynovsky Valentin. All rights reserved.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

import datetime


def calendar(not_ms: bool = True) -> datetime:
	"""
	It returns the current date and time.

	:param not_ms: If True, the microseconds will be set to 0, defaults to True
	:type not_ms: bool (optional)
	:return: A datetime object with the current date and time.
	"""
	if not_ms:
		return datetime.datetime.today().replace(microsecond=0)
	return datetime.datetime.today()
