from tasks import building_fort, mining, foraging, building_farm


def get_tasks():
    result = {
        foraging.task.name: foraging.task,
        mining.task.name: mining.task,
        building_farm.task.name: building_farm.task,
        building_fort.task.name: building_fort.task
    }

    return result
