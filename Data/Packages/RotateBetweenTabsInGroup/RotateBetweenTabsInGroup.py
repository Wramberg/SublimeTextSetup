import sublime
import sublime_plugin

class RotateToNextTabInGroup(sublime_plugin.WindowCommand):
   def run(self):
      active_view = self.window.active_view()
      active_grp, index = self.window.get_view_index(active_view)
      views = self.window.views_in_group(active_grp)
      next_index = (index + 1) % len(views)
      self.window.focus_view(views[next_index])


class RotateToPrevTabInGroup(sublime_plugin.WindowCommand):
   def run(self):
      active_view = self.window.active_view()
      active_grp, index = self.window.get_view_index(active_view)
      views = self.window.views_in_group(active_grp)
      next_index = (index - 1) % len(views)
      self.window.focus_view(views[next_index])
