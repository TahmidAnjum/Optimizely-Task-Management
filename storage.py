from utils import Utils

class Storage:
	def __init__(self):
		self.tasks = Utils.get_tasks()

	def save_task(self, task):
		self.tasks.append(task)
		Utils.add_task(task=task)

	def update_task(self, updated_task):
		for i, task in enumerate(self.tasks):
			if task.title == updated_task.title:
				self.tasks[i] = updated_task
				Utils.update_task(index=i, updated_task=task)
				break

	def get_task(self, title):
		for task in self.tasks:
			if task.title == title:
				return task
		return None

	def get_all_tasks(self):
		return list(self.tasks)

	def clear_all_tasks(self):
		self.tasks = []
		Utils.initialize_shelve(reinitialize=True)
