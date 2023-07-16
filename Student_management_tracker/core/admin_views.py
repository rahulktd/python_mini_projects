from django.shortcuts import render, redirect, get_object_or_404

from core.filters import StudentFilter
from core.forms import ReplyForm, NotificationForm
from core.models import Students, Complaint, Reply, Notification


def view_students(request):
    data = Students.objects.filter(is_student=True)
    stu = StudentFilter(request.GET, queryset=data)
    stu_list = stu.qs
    return render(request,'Admin/view_students.html',{'data':stu_list,'stu':stu})

def activate_student(request,id):
    student = Students.objects.get(id=id)
    if request.method == 'POST':
        student.is_active = True
        student.save()
        return redirect('admin_dashboard')
    return render(request, 'Admin/activate_student.html', {'student': student})

def complaints_to(request):
    data = Complaint.objects.all()
    return render(request,'Admin/complaints_to.html',{'data':data})

def reply_to_complaint(request, id):
    complaint = Complaint.objects.get(id=id)
    replies = Reply.objects.filter(complaint=complaint).order_by('created_at')
    if request.method == 'POST':
        form = ReplyForm(request.POST)
        if form.is_valid():
            content = form.cleaned_data['content']
            reply = Reply(complaint=complaint, content=content)
            reply.form.save()
            notification_content = "Your complaint (ID: {complaint.id}) has a new reply."
            notification = Notification(student=complaint.student, content=notification_content)
            notification.save()

            return redirect('admin_dashboard')

    else:
        form = ReplyForm()

    return render(request, 'Admin/reply_to_complaint.html', {'form': form, 'complaint': complaint, 'replies': replies})

def send_notification(request,id):
    complaint = get_object_or_404(Complaint, id=id)

    if request.method == 'POST':
        form = ReplyForm(request.POST)
        if form.is_valid():
            content = form.cleaned_data['content']
            reply = Reply(complaint=complaint, content=content)
            reply.save()

            notification_content = f"Your complaint (ID: {complaint.id}) has been replied: {content}"
            notification = Notification(student=complaint.student, content=notification_content)
            notification.save()

            return redirect('admin_dashboard')

    else:
        form = ReplyForm()

    return render(request, 'Admin/send_reply.html', {'form': form, 'complaint': complaint})
