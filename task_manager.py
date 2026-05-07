from tasks import mining, foraging, building_farm


def get_tasks():
    result = {
        foraging.task.name: foraging.task,
        mining.task.name: mining.task,
        building_farm.task.name: building_farm.task
    }

    return result
