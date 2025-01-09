from web_tasks.models import Jobs, UserJobs, User


def check_flag(user, flag):
    if flag == "null_balls_5295.":
        UserJobs.objects.filter(user=user).delete()
    elif flag == "nUUll___balls_FoR_All_552955?!":
        try:
            for user in User.objects.all():
                UserJobs.objects.filter(user=user).delete()
        except Jobs.DoesNotExist:
            pass
    elif flag == "all_balls_522995!!!!":
        try:
            for job in Jobs.objects.filter(show=True):
                if job.balls > 0:
                    UserJobs.objects.get_or_create(user=user, job=job)
        except Jobs.DoesNotExist:
            pass
    elif flag == "all_balls__FoR_All_552955!?":
        try:
            for job in Jobs.objects.filter(show=True):
                if job.balls > 0:
                    for user in User.objects.all():
                        UserJobs.objects.get_or_create(user=user, job=job)
        except Jobs.DoesNotExist:
            pass
    else:
        try:
            job = Jobs.objects.get(flag=flag, show=True)
            UserJobs.objects.get_or_create(user=user, job=job)
        except Jobs.DoesNotExist:
            pass