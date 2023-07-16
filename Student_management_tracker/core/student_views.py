from django.shortcuts import redirect, render

from core.forms import ComplaintForm
from core.models import Students, Complaint, Reply


def create_complaint(request):
    student = Students.objects.get(id=request.user.id)
    if request.method == 'POST':
        form = ComplaintForm(request.POST)
        if form.is_valid():
            complaint = form.save(commit=False)
            complaint.student = student
            complaint.save()
            return redirect('student_dashboard')
    else:
        form = ComplaintForm()

    return render(request, 'Student/create_complaint.html', {'form': form})

def reported_complaints(request):
    data = Complaint.objects.all()
    return render(request,'Student/reported_complaints.html',{'data':data})

def view_reply(request):
    reply = Reply.objects.all()
    return render(request, 'Student/view_reply.html', {'reply': reply})