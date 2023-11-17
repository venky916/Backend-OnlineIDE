import uuid
import subprocess
import django
django.setup()
from .models import Submissions

def create_code_file(code,language):
    file_name=str(uuid.uuid4())+"."+language
    with open("code/"+file_name,"w") as f:
        f.write(code)
    
    return file_name


def execute_file(file_name,language,submission_id):
    submission=Submissions.objects.get(pk=submission_id)
    if language=="py":
        # subprocess.call(["python","code/"+file_name])
        result=subprocess.run(["python","code/"+file_name],stdout=subprocess.PIPE)
        if result.returncode==1:# both runtime time and compile time error
            submission.status='E'
            submission.save()
            return
        output= result.stdout
        submission.output=output.decode("utf-8")
        submission.status='S'
        submission.save()