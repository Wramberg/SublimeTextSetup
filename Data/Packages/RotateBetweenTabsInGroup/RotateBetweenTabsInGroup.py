import sublime
import sublime_plugin

class RotateToNextTabInGroup(sublime_plugin.WindowCommand):
   def run(self):
      active_view = self.window.active_view()
      active_grp, index = self.window.get_view_index(active_view)
      views = self.window.views_in_group(active_grp)

      if index == (len(views) - 1):
         next_index = 0
      else:
         next_index = index + 1

      self.window.focus_view(views[next_index])


class RotateToPrevTabInGroup(sublime_plugin.WindowCommand):
   def run(self):
      active_view = self.window.active_view()
      active_grp, index = self.window.get_view_index(active_view)
      views = self.window.views_in_group(active_grp)

      if index == 0:
         next_index = len(views) - 1
      else:
         next_index = index - 1

      self.window.focus_view(views[next_index])
