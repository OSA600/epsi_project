from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Message, Employee, TypeDemande, Acces, Ordinateur, Telephone, Service
from pprint import pprint


def index(request):
    # render (request, "templates")
    if 'user_id' not in request.session:
        data = request.POST
        error = False
        if data:
            if 'uname' in data:
                try:
                    emp = Employee.objects.get(name=request.POST['uname'])
                    if emp.password == request.POST['psw']:
                        request.session['user_id'] = emp.id
                        obj = Message.objects.filter(receiver=emp.service).filter(valid=False)
                        return render(request, "message/index.html", context={"Messages": obj, "emp": emp})
                    else:
                        return HttpResponse("Mot de passe incorrecte.")
                except:
                    return HttpResponse("Cet utilisateur  n'existe pas.")
            else:
                return HttpResponse("Veuillez saisir l'utilisateur.")
        else:
            return render(request, "index.html")
    else:
        id = request.session['user_id']
        emp = Employee.objects.get(id=id)
        obj = Message.objects.filter(receiver=emp.service).filter(valid=False)
        return render(request, "message/index.html", context={"Messages": obj, "emp": emp})


def messageDetail(request, id):
    obj = Message.objects.get(id=id)
    return render(request, 'message/messageDetail.html', {'valeur': obj})


def envoyerMessage(request):
    return render(request, 'message/formMessage.html')


def addRequest(request):
    user = request.session['user_id']
    user = Employee.objects.get(id=user)
    objTypes = TypeDemande.objects.all()
    objEmployees = Employee.objects.filter(refOrdi=None)
    objAcces = Acces.objects.all()
    objOrdinateur = Ordinateur.objects.all()
    objTelephone = Telephone.objects.all()
    service = Service.objects.all()
    return render(request, 'message/formRequest.html',
                  {'typeDemandes': objTypes, 'sendBy': user.service, 'employees': objEmployees, 'acces': objAcces,
                   'ordinateurs': objOrdinateur, 'telephones': objTelephone, 'services': service})


def saveRequest(request):
    error = False
    if request.POST:
        data = request.POST
        print(data)
        if 'typeDemande' in data:
            typeDemande = data.get('typeDemande')
            typeDemande = TypeDemande.objects.get(id=typeDemande)
            employee = data.get('employee')
            employee = Employee.objects.get(id=employee)
            sendBy = data.get('sendBy')

            receiver = data.get('service')
            receiver = Service.objects.get(id=receiver)
            print(receiver)
            description = data.get('description')
        else:
            error = True

        if 'refAcces' in data and data.get('refAcces') != "":
            refAcces = data.get('refAcces')
            refAcces = Acces.objects.get(id=refAcces)
        else:
            refAcces = ""

        if 'refOrdi' in data and data.get('refOrdi') != "":
            refOrdi = data.get('refOrdi')
            refOrdi = Ordinateur.objects.get(id=refOrdi)
        else:
            refOrdi = ""

        if 'refPhone' in data and data.get('refPhone') != "":
            refPhone = data.get('refPhone')
            refPhone = Telephone.objects.get(id=refPhone)
        else:
            refPhone = ""

        if not error:
            id = request.session['user_id']
            emp = Employee.objects.get(id=id)
            service = request.POST.get('service')
            print(service)
            service_id = Service.objects.filter(libelle=service)
            # print(receiver)
            # obj = Message.objects.filter(receiver=service_id.id)

            newMessage = Message(typeDemande=typeDemande, ordinateur=refOrdi, telephone=refPhone, acces=refAcces,
                                 description=description, employe=employee, sendBy=sendBy, receiver=receiver)
            newMessage.save()
            print(str(newMessage))
            obj = {}
            return render(request, "message/index.html", context={"Messages": obj, "emp": emp})
        else:
            return HttpResponse("type demande obligatoire ")

    else:
        return HttpResponse("there is an error ")


def sysadmin(request, id):
    objAcces = Acces.objects.all()
    objOrdinateur = Ordinateur.objects.all()
    objTelephone = Telephone.objects.all()
    emp = Message.objects.get(id=id)

    return render(request, "ASaffichage.html", {'valeur': emp})


def indexall(request):
    msg = Message.objects.all()

    return render(request, "message/indexmessages.html", context={"Messages": msg})


def ficheRequest(request, reference):
    info = Employee.objects.get(reference=reference)

    return render(request, "message/fiche.html", {'valeur': info
                                                  })


def validRequest(request, id):
    try:
        # obj = Message.objects.filter(id=id)
        obj = Message.objects.filter(id=id).update(valid=True)
        return redirect("/messages")
    except:
        return HttpResponse(id)


def refuseRequest(request, id):
    try:
        # obj = Message.objects.filter(id=id)
        obj = Message.objects.filter(id=id).update(is_active=False)
        user = request.session['user_id']
        user = Employee.objects.get(id=user)
        objTypes = TypeDemande.objects.all()
        objEmployees = Employee.objects.filter(refOrdi=None)
        objAcces = Acces.objects.all()
        objOrdinateur = Ordinateur.objects.all()
        objTelephone = Telephone.objects.all()
        return render(request, 'message/formRequest.html',
                      {'typeDemandes': objTypes, 'sendBy': user.service, 'employees': objEmployees, 'acces': objAcces,
                       'ordinateurs': objOrdinateur, 'telephones': objTelephone})

    except:
        return HttpResponse(id)


def logOut(request):
    del request.session['user_id']
    return render(request, 'index.html')
