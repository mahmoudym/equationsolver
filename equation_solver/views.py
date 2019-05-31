from __future__ import print_function
from django.shortcuts import render
from equation_solver.models import Equation_solver
from equation_solver.models import Folder
from equation_solver.equation import executeEq

def welcome(request):
    return render(request,'welcome.html',{})

def equation_folder(request):
    folders = Folder.objects.all()
    context = {
        'folders':folders
    }
    if (folders!=None):
        return render(request, 'equation_folder.html',context)
    else:
        return render(request, 'equation_folder.html',{})

def equation_index(request,pk):
    equations = Equation_solver.objects.filter(folder = pk)

    context = {
        'equations': equations,
        'folderpk' : pk
    }
    if (equations!=None):
        return render(request, 'equation_index.html',context)
    else:
        return render(request, 'equation_index.html',{})

def equation_detail(request, pk):
    equation = Equation_solver.objects.get(pk = pk)
    context = {
        'equation': equation,
        'variables': equation.variables.split(","),
        'result' : str(0)
    }
    return render(request,'equation_detail.html',context)

def createfolder(request):
    f = Folder()
    f.name = request.POST.get('name')
    f.save()
    folders = Folder.objects.all()
    context = {
        'folders':folders
    }
    return render(request,'equation_folder.html',context)

def deletefolder(request, pk):
    Folder.objects.filter(pk=pk).delete()
    Equation_solver.objects.filter(folder=pk).delete()
    folders = Folder.objects.all()
    context = {
        'folders':folders
    }
    return render(request,'equation_folder.html',context)

def createequation(request, pk):
    e = Equation_solver()
    e.name = request.POST.get('name')
    e.equation = request.POST.get('equation')
    e.variables = request.POST.get('variables')
    e.description = request.POST.get('description')
    e.folder = pk
    e.save()
    equations = Equation_solver.objects.filter(folder = pk)
    context = {
        'equations': equations,
        'folderpk' : pk
    }
    return render(request, 'equation_index.html',context)

def deleteequation(request,pk):
    x = Equation_solver.objects.get(pk=pk)
    pkk = x.folder
    x.delete()
    equations = Equation_solver.objects.filter(folder = pkk)
    context = {
        'equations': equations,
        'folderpk' : pkk
    }
    return render(request, 'equation_index.html',context)

def solve(request, pk):
    x = Equation_solver.objects.get(pk = pk)
    variables = x.variables.split(",")
    st = ""
    st+= variables[0] + " = " + request.POST.get(variables[0])
    if len(variables)>1:
        for i in variables[1:]:
            st += "," +  i + " = " + request.POST.get(i)
    res = executeEq(x.equation,st)
    context = {
        'equation': x,
        'variables': x.variables.split(","),
        'result': str(res)
    }
    return render(request, 'equation_detail.html',context)
