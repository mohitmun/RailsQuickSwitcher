import unicodedata
import os, fnmatch 
import sublime, sublime_plugin,re

class QmCommand(sublime_plugin.TextCommand):
    def run(self,edit):
        current_file_path = self.view.file_name()
        regex = re.compile(r'(.*?app)/views/(.*?)s/.*')
        current_file_path = regex.sub(r'\1/models/\2.rb', current_file_path)
        regex = re.compile(r'(.*?app)/controllers/(.*?)s_controller.rb')
        current_file_path = regex.sub(r'\1/models/\2.rb', current_file_path)
        # current_file_path = re.sub(r"/controllers | /views//.*","/models",current_file_path)
        # current_file_path = re.sub(r"_controller.rb",".rb",current_file_path)
        # final_path = current_file_path + "/" + line_contents + ".html.haml"
        print "qm is getting called" + current_file_path
        if current_file_path != "":
            self.view.window().open_file(current_file_path,sublime.ENCODED_POSITION)

class QvCommand(sublime_plugin.TextCommand):
    def run(self,edit):
        for region in self.view.sel():
            regions = self.view.find_all("def ",sublime.LITERAL)
            for def_region in regions:
                if def_region.begin() > region.begin():
                    print type(regions)
                    line = self.view.line(regions[regions.index(def_region) - 1])
                    line_contents = self.view.substr(line)
                    line_contents = re.sub(r"\(.*\)","",line_contents)
                    line_contents = re.sub(r"def ","",line_contents)
                    current_file_path = self.view.file_name()
                    current_file_path = re.sub(r"controllers","views",current_file_path)
                    current_file_path = re.sub(r"_controller.rb","",current_file_path)
                    final_path = current_file_path + "/" + line_contents + ".html.haml"
                    final_path = re.sub(r"\s","",final_path)
                    accurate_path = find(re.sub(r"\s","",line_contents) + ".*" , current_file_path)
                    if accurate_path != "":
                        self.view.window().open_file(accurate_path,sublime.ENCODED_POSITION)
                    break

class QcCommand(sublime_plugin.TextCommand):
    def run(self,edit):
        current_file_path = self.view.file_name()
        regex = re.compile(r'(.*?app)/views/(.*?)/.*')
        current_file_path = regex.sub(r'\1/controllers/\2_controller.rb', current_file_path)
        regex = re.compile(r'(.*?app)/models/(.*?).rb')
        current_file_path = regex.sub(r'\1/controllers/\2s_controller.rb', current_file_path)
        # current_file_path = re.sub(r"/controllers | /views//.*","/models",current_file_path)
        # current_file_path = re.sub(r"_controller.rb",".rb",current_file_path)
        # final_path = current_file_path + "/" + line_contents + ".html.haml"
        print "qm is getting called" + current_file_path
        if current_file_path != "":
            self.view.window().open_file(current_file_path,sublime.ENCODED_POSITION)


def find(pattern, path):
    for root, dirs, files in os.walk(path):
        result = ""
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                print "n: " + name
                print "p: " + pattern
                print "nmatch: " + str(fnmatch.fnmatch(name, pattern))
                result = os.path.join(root, name)
                print "result: " + result 
                break
        return result