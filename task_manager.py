from tasks import mining, foraging


def get_tasks():
    result = {
        foraging.task.name: foraging.task,
        mining.task.name: mining.task
    }

    return result
