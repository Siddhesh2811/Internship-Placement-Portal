from django import template
from dashboard.models import Student_placement, Student_internship, studentUser, placementInfo, internshipInfo
register = template.Library()


@register.filter(name="is_student")
def is_student(user, suser):
    for u in suser:
        if(u.username == user.username):
            return True
    return False


@register.filter(name="student_yourname")
def student_yourname(username, suser):
    for u in suser:
        if(u.username == username):
            return u.yourname


@register.filter(name="email")
def email(username, suser):
    for u in suser:
        if(u.username == username):
            return u.email


@register.filter(name="student_branch")
def student_branch(username, suser):
    for u in suser:
        if(u.username == username):
            return u.branch


@register.filter(name="yog")
def yog(username, suser):
    for u in suser:
        if(u.username == username):
            return u.yog


@register.filter(name="contact")
def contact(username, suser):
    for u in suser:
        if(u.username == username):
            return u.contact


@register.filter(name="company_name")
def company_name(username, cuser):
    for u in cuser:
        if(u.username == username):
            return u.companyname


@register.filter(name="address")
def address(username, cuser):
    for u in cuser:
        if(u.username == username):
            return u.address


@register.filter(name="company_email")
def company_email(username, cuser):
    for u in cuser:
        if(u.username == username):
            return u.companyemail


@register.filter(name="complacement")
def complacement(email, pinfo):
    for p in pinfo:
        if(email == p.company_email):
            return p


@register.filter(name="complacementcount")
def complacementcount(user, pObj):
    return len(pObj)


@register.filter(name="cominternshipcount")
def cominternshipcount(user, iObj):
    return len(iObj)


@register.filter(name="notapprovecom")
def notapprovecom(iObj, pObj):
    c = 0
    for p in pObj:
        if not p.status:
            c += 1
    for i in iObj:
        if not i.status:
            c += 1
    return c


@register.filter(name="approvecom")
def approvecom(iObj, pObj):
    c = 0
    for p in pObj:
        if p.status:
            c += 1
    for i in iObj:
        if i.status:
            c += 1
    return c


@register.filter(name="stuplacementcount")
def stuplacementcount(user, pObj):
    c = 0
    for p in pObj:
        if p.status:
            c += 1
    return c


@register.filter(name="stuinternshipcount")
def stuinternshipcount(user, iObj):
    c = 0
    for i in iObj:
        if i.status:
            c += 1
    return c


@register.filter(name="placementStatus")
def placementStatus(user, id):
    try:
       studentUsername = studentUser.objects.get(user=user)
       placementId = placementInfo.objects.get(id=id)
       stuPlaceObj = Student_placement.objects.get(
       student_username=studentUsername, placement_id=placementId)
       if (stuPlaceObj.status):
           return True
       else:
           return False
    except:
       return False

@register.filter(name="internshipStatus")
def internshipStatus(user, id):
   try:
       studentUsername = studentUser.objects.get(user=user)
       internshipId = internshipInfo.objects.get(id=id)
       stuInternObj = Student_internship.objects.get(
       student_username=studentUsername, internship_id=internshipId)
       if (stuInternObj.status):
           return True
       else:
           return False
   except:
       return False

@register.filter(name="pendingintern")
def pendingintern(user,id):
    try:
       studentUsername = studentUser.objects.get(user=user)
       internshipId = internshipInfo.objects.get(id=id)
       stuInternObj = Student_internship.objects.get(
       student_username=studentUsername, internship_id=internshipId)
       if (stuInternObj.pending):
           return True
       else:
           return False
    except:
       return False

@register.filter(name="pendingplace")
def pendingplace(user, id):
    try:
       studentUsername = studentUser.objects.get(user=user)
       placementId = placementInfo.objects.get(id=id)
       stuPlaceObj = Student_placement.objects.get(
       student_username=studentUsername, placement_id=placementId)
       if (stuPlaceObj.pending):
           return True
       else:
           return False
    except:
       return False

@register.filter(name="stucount")
def stucount(user, id):
    c=0
    try:
        studentUsername = studentUser.objects.get(user=user)
        try:
            stuPlaceObj = Student_placement.objects.all()
            for s in stuPlaceObj:
                if s.student_username == studentUsername and s.status == True:
                    c+=1
        except:
            c+=0
        try:
            stuInternObj = Student_internship.objects.all()
            for s in stuInternObj:
                if s.student_username == studentUsername and s.status == True:
                    c+=1
        except:
            c+=0
        return c

    except:
        return 0

@register.filter(name="notapplied")
def notapplied(user, id):
    c = 0
    c1 = 0
    pObj= placementInfo.objects.all()
    iObj = internshipInfo.objects.all()
    for p in pObj:
        if p.status:
            c += 1
    for i in iObj:
        if i.status:
            c += 1
    c1 = stucount(user, id)
    return c-c1
    
