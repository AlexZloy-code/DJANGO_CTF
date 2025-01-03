from main.models import Jobs, UserJobs


def check_flag(user, flag):
    if flag == "null":
        UserJobs.objects.filter(user=user).delete()
    else:
        try:
            job = Jobs.objects.get(flag=flag)
            UserJobs.objects.get_or_create(user=user, job=job)
        except Jobs.DoesNotExist:
            pass
