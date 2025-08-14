from web_tasks.models import Jobs, UserJobs, User


def check_flag(user, flag, admin):
    if admin:
        if flag == "null_balls":
            UserJobs.objects.filter(user=user).delete()
            messange = 'secsess'
        elif flag == "null_balls_for_all":
            try:
                for user in User.objects.all():
                    UserJobs.objects.filter(user=user).delete()
                messange = 'secsess'
            except Jobs.DoesNotExist:
                pass
        elif flag == "all_balls":
            try:
                for job in Jobs.objects.filter(show=True):
                    if job.balls > 0:
                        UserJobs.objects.get_or_create(user=user, job=job)
                messange = 'secsess'
            except Jobs.DoesNotExist:
                pass
        elif flag == "all_balls_for_all":
            try:
                for job in Jobs.objects.filter(show=True):
                    if job.balls > 0:
                        for user in User.objects.all():
                            UserJobs.objects.get_or_create(user=user, job=job)
                messange = 'secsess'
            except Jobs.DoesNotExist:
                pass
        
        try:
            return messange
        except Exception:
            pass

    try:
        job = Jobs.objects.get(flag=flag, show=True)
        st_pos = len(UserJobs.objects.all())
        UserJobs.objects.get_or_create(user=user, job=job)
        if st_pos == len(UserJobs.objects.all()):
            messange = 'repeat'
        else:
            messange = 'correct'
    except Jobs.DoesNotExist:
        messange = 'incorrect'

    return messange