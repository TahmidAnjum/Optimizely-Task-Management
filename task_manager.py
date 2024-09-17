from datetime import datetime


class Task:

	def __init__(self, title, description):
		self.title = title
		self.description = description
		self.completed = False
		self.created_at = datetime.now().isoformat()
	
	def complete(self):
		self.completed_at = datetime.now().isoformat()


class TaskManager:

	def __init__(self, storage):
		self.storage = storage

	def add_task(self, title, description):
		task = Task(title, description)
		self.storage.save_task(task)
		return task

	def complete_task(self, title):
		task = self.storage.get_task(title)
		if task:
			task.completed = True
			task.complete()
			self.storage.update_task(task)
			return True
		return False

	def list_tasks(self, include_completed=False):
		tasks = self.storage.get_all_tasks()
		return tasks if include_completed else [task for task in tasks if task.completed]
	
	def print_all_tasks(self):
		tasks = self.storage.get_all_tasks()
		for task in tasks:
			print(vars(task))
	
	def get_average_completion_time(self):
		tasks = self.storage.get_all_tasks()
		total_time = 0
		total_completed = 0
		for task in tasks:
			if task.completed:
				total_completed += 1
				total_time += task.completed_at - task.created_at
		if total_completed == 0:
			return 0
		else: 
			return total_time / total_completed



	def generate_report(self):
		tasks = self.storage.get_all_tasks()
		total_tasks = len(tasks)
		completed_tasks = len([task for task in tasks if task.completed])

		report = {
		    "total": total_tasks,
		    "completed": completed_tasks,
		    "pending": total_tasks - completed_tasks,
			"average time" : self.get_average_completion_time()
		}

		return report

