""" =====================================================================
File:        TypoFinder.py
Description: Sublime Text 3 plugin for finding and replacing common typos
Maintainer:  pszucs <https://github.com/pszucs>
License:     BSD, see LICENSE for more details.
Website:     https://github.com/pszucs/TypoFinder
======================================================================"""

import sublime
import sublime_plugin

SETTINGS_FILE = 'TypoFinder.sublime-settings'

class TypoFinder(sublime_plugin.EventListener):
    def on_post_save(self, view):
        global_settings = sublime.load_settings(SETTINGS_FILE)
        should_run = global_settings.get('typo_on_save') and SETTINGS_FILE not in view.file_name()
        auto_correct = global_settings.get('auto_correct')
        dictionary = global_settings.get("dictionary")
        
        if should_run is True:
            # read file line by line
            lines = view.substr(sublime.Region(0, view.size())).split("\n")

            for idx, val in enumerate(lines):
                for elem in dictionary:
                    for key in elem:
                        typo = key
                        fix = elem[key]
                        pos = val.find(typo)

                        if pos != -1:
                            # scroll to the line and select the word
                            pt = view.text_point(idx, pos)
                            pt2 = view.text_point(idx, pos + len(typo))
                            view.sel().clear()
                            view.sel().add(sublime.Region(pt, pt2))
                            view.show(pt)
                            if auto_correct is True:
                                fix_it = sublime.ok_cancel_dialog('Typo found in line ' + str(idx + 1) + '.', "Fix it!")
                                if fix_it:
                                    view.run_command("replace_typo", {"row": pt, "col": pt2, "fix": fix})

class ReplaceTypoCommand(sublime_plugin.TextCommand):
    def run(self, edit, row, col, fix):
        self.view.replace(edit, sublime.Region(row, col), fix)
