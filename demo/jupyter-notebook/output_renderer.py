#
# Copyright 2019 AXA Group Operations S.A.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import uuid
import json
from IPython.display import display, Markdown, display_html, display_javascript, HTML
from pygments import highlight
from pygments.lexers import JsonLexer
from pygments.formatters import TerminalFormatter

class RenderJSON(object):
    def __init__(self, data):
        self.render_json(data)
    def render_json(self, data):
        json_object = json.loads(json.dumps(data))
        json_str = json.dumps(json_object, indent=4, sort_keys=True)
        print(highlight(json_str, JsonLexer(), TerminalFormatter()))

class RenderBigJSON(object):
    def __init__(self, json_data):
        if isinstance(json_data, dict) or isinstance(json_data, list):
            self.json_str = json.dumps(json_data)
        else:
            self.json_str = json_data
        self.uuid = str(uuid.uuid4())

    def _ipython_display_(self):
        display_html('<div id="{}" style="height: 600px; width:100%;font: 12px/18px monospace !important;"></div>'.format(self.uuid), raw=True)
        display_javascript("""
        require(["https://rawgit.com/caldwell/renderjson/master/renderjson.js"], function() {
            renderjson.set_show_to_level(2);
            document.getElementById('%s').appendChild(renderjson(%s))
        });
      """ % (self.uuid, self.json_str), raw=True)

class RenderMarkdown(object):
    def __init__(self, markdown_data):
        self.markdown_data = markdown_data
        self.uuid = str(uuid.uuid4())

    def _ipython_display_(self):
        display(Markdown(self.markdown_data))

class RenderHTML(object):
    def __init__(self, html_data):
        self.html_data = html_data
        self.uuid = str(uuid.uuid4())

    def _ipython_display_(self):
        display(HTML(self.html_data))