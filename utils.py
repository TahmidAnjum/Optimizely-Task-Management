import shelve

class Utils:
    @staticmethod
    def initialize_shelve(reinitialize=False):
        with shelve.open('db') as db:
            if reinitialize == True or 'tasks' not in db:
                db['tasks'] = []

    @staticmethod
    def get_tasks():
        with shelve.open('db') as db:
            return db['tasks']
        
    @staticmethod
    def add_task(task):
         with shelve.open('db') as db:
            tasks = db['tasks']
            tasks.append(task)
            db['tasks'] = tasks

        
    @staticmethod
    def update_task(index, updated_task):
         with shelve.open('db') as db:
            tasks = db['tasks']
            tasks[index] = updated_task
            db['tasks'] = tasks
        
    

