activities = {"running": {"health": ((3, 180), (1,)), "hedons": ((2, 10), (-2,)), "is_tiring": True}, 
              "textbooks": {"health": ((2,),), "hedons": ((1, 20), (-1,)), "is_tiring": True}, 
              "resting": {"health": ((0,),), "hedons": ((0,),), "is_tiring": False}
              }


def is_timed(item):
    """Check if a stat item has a timed increment. item = (x,) or (x, y)"""
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
    global bored

    if last_two_stars[0] < 120:
        bored = True
    else:
        star = activity
        last_two_stars = [last_two_stars[1], 0]

def earnings(stats, duration, earlier, tired):
    """Compute how many points are earned by doing an activity"""
    gained = 0
    remaining_time = duration+earlier
    for stat in stats:
        amount = stat[0] if time_since_tiring >= 120 or not tired else -2
        time = min(remaining_time, stat[1]) if is_timed(stat) else remaining_time

        if remaining_time > duration:
            remaining_time -= time
            time, earlier = time-min(earlier, time), earlier-min(earlier, time)
        else:
            remaining_time -= time

        gained += amount*time

        if remaining_time == 0: break

    return gained


def perform_activity(activity, duration):
    """Simulate the user's performing activity, activity for duration minutes.
    activity must be one of"running","textbooks", or"resting". duration must be a positive int"""
    global health
    global hedons
    global time_since_tiring
    global star
    global last_two_stars
    global previous_activity

    #add three hedons each min for the first five mins with a star if the activities match
    if star_can_be_taken(activity):
        hedons += min(10, duration)*3
    star = None

    earlier = 0 if activity != previous_activity[0] else previous_activity[1]
    previous_activity = [activity, duration]
    activity = activities[activity]

    health += earnings(activity["health"], duration, earlier, False)
    hedons += earnings(activity["hedons"], duration, earlier, activity["is_tiring"])

    #resets or increments the tired counter
    if activity["is_tiring"]:
        time_since_tiring = 0
    else:
        time_since_tiring += duration

    if not bored:
        last_two_stars = [x+duration for x in last_two_stars]


def star_can_be_taken(activity):
    """Return True iff a star can be used to get more hedons if done with activity activity"""
    return star == activity and not bored


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
    global bored
    global previous_activity

    hedons = 0
    health = 0
    time_since_tiring = 120
    star = None
    last_two_stars = [120, 120]
    bored = False
    previous_activity = [None, 0]



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