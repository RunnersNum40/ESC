activities = {"running": {"health": ((3, 180), 1), "hedons": ((2, 10), (-2,)), "is_tiring": True}, 
              "textbooks": {"health": ((2,),), "hedons": ((1, 20), (-1,)), "is_tiring": True}, 
              "resting": {"health": ((0,),), "hedons": ((0,),), "is_tiring": False}
              }


def is_timed(item):
    try:
        item[1]
    except Exception:
        return False
    else:
        return True


def get_cur_hedons():
    """Return the number of hedons that the user has accumulated so far."""
    return hedons


def get_cur_health():
    """Return the number of health points that the user has accumulated so far."""
    return health


def offer_star(activity):
    """Simulate offering the user a star for engaging in the exercise activity.
    Assume activity is a string, one of "running","textbooks", or "resting"."""
    global last_two_stars
    global star
    global tired

    if last_two_stars[0] < 120:
        tired = True
    else:
        star = activity
        last_two_stars = [last_two_stars[1], 0]


def perform_activity(activity, duration):
    """Simulate the user's performing activity, activity for duration minutes.
    activity must be one of"running","textbooks", or"resting". duration must be a positive int"""
    global health
    global hedons
    global time_since_tiring
    global star
    global last_two_stars

    if star == activity:
        hedons += min(10, duration)*3
    star = None

    activity = activities[activity]

    remaining_time = duration
    for stat in activity["health"]:
        amount = stat[0]
        time = min(remaining_time, stat[1]) if is_timed(stat) else remaining_time
        health += amount*time

        remaining_time -= time
        if remaining_time == 0: break

    remaining_time = duration
    for stat in activity["hedons"]:
        amount = stat[0] if time_since_tiring >= 120 or not activity["is_tiring"] else -2
        time = min(remaining_time, stat[1]) if is_timed(stat) else remaining_time
        hedons += amount*time

        remaining_time -= time
        if remaining_time == 0: break

    if activity["is_tiring"]:
        time_since_tiring = 0
    else:
        time_since_tiring += duration

    if not tired:
        last_two_stars = [x+duration for x in last_two_stars]


def star_can_be_taken(activity):
    """Return True iff a star can be used to get more hedons if done with activity activity"""
    return star == activity and not tired


def most_fun_activity_minute():
    """Return the activity which would give the most hedones if preformed for one minute"""
    return sorted(activities.keys(), key=lambda activity: (activities[activity]["hedons"][0][0] if time_since_tiring >= 120 or not activities[activity]["is_tiring"] else -2)+3*(star == activity), reverse=True)[0]


def initialize():
    """Initialize all global variables"""
    global hedons
    global health
    global time_since_tiring
    global star
    global last_two_stars
    global tired

    hedons = 0
    health = 0
    time_since_tiring = 120
    star = None
    last_two_stars = [120, 120]
    tired = False



if __name__ == '__main__':
    initialize()
    perform_activity("running", 30)
    print(get_cur_hedons())            # -20 = 10 * 2 + 20 * (-2)
    print(get_cur_health())            # 90 = 30 * 3
    print(most_fun_activity_minute())  #resting
    perform_activity("resting", 30)
    offer_star("running")
    print(most_fun_activity_minute())  # running
    perform_activity("textbooks", 30)
    print(get_cur_health())            # 150 = 90 + 30*2
    print(get_cur_hedons())            # -80 = -20 + 30 * (-2)
    offer_star("running")
    perform_activity("running", 20)
    print(get_cur_health())            # 210 = 150 + 20 * 3
    print(get_cur_hedons())            # -90 = -80 + 10 * (3-2) + 10 * (-2)
    perform_activity("running", 170)
    print(get_cur_health())            # 700 = 210 + 160 * 3 + 10 * 1
    print(get_cur_hedons())            # -430 = -90 + 170 * (-2)