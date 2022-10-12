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

import sys

from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication

from ui.keylogger import KeyLogger


if __name__ == '__main__':
    while True:
        app = QApplication(sys.argv)
        ui = KeyLogger()
        ui.show()
        app.exec()
        if not ui.REBOOT:
            break  # If the program did not reset the data, exit the cycle and close the program
        app = None

    sys.exit()
