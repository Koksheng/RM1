from django.shortcuts import render
from dashboard.forms import *
from dashboard.models import *
from django.http import JsonResponse
from django.template.loader import render_to_string
import pandas as pd
import os
from datetime import timedelta, datetime
from django.conf import settings
import json



# Create your views here.
def home_view(request):
    context = {}
    project_id = 'asmprojectno123'
    sheetname = "PRS (Top Level Requirement)_DM"
    # excel_path = "D:\work\Requirement Management\\" + sheetname + ".xlsx"
    excel_path = settings.EXCEL_PATH + sheetname + ".xlsx"
    dbframe = pd.read_excel(excel_path, sheet_name=sheetname)
    for df in dbframe.itertuples():
        id = project_id+ '_' + str(df.ID)
        mr_exists = MachineRequirement.objects.filter(id=id).first()
        if mr_exists == None:
            obj = MachineRequirement.objects.create(id=id, project_id=project_id, prs_id=df.ID, title=df.Title, area=df.Area, description=df.Description, priority=df.Priority, category=df.Category, status=df.Status, type=df.Type, remarks=df.Remarks, created_at=datetime.now())
            obj.save()
    return render(request, 'dashboard/home.html', context)

def machinerequirement_view(request):
    machinerequirement_object = MachineRequirement.objects.all().order_by('project_id','prs_id')
    context = {"machinerequirementobject": machinerequirement_object}
    return render(request, 'dashboard/machinerequirement.html', context)

def modulerequirement_view(request):
    modulerequirement_object = ModuleRequirement.objects.all().order_by('id')
    context = {"modulerequirementobject": modulerequirement_object}
    return render(request, 'dashboard/modulerequirement.html', context)

def save_modulerequirement_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            old_status = form.initial['status']
            df = "324"
            # new_status = form.data['status']
            # transnum = form.data['transducer_serial_no']
            # process_stage_id = form.data['current_stage']
            # stage_profile = form.data['stage_profile']
            form.save()
            # data['form_is_valid'] = True
            # # update status into BurnIn Log tbl if operator update status in dashboard
            # if old_status!=new_status:
            #     processstage = ProcessStage.objects.get(id = process_stage_id, stage_profile = stage_profile)
            #     software = processstage.general_process_stage.software
            #     if software == "Burn In":
            #         BILog.objects.filter(transducer_serial_no=transnum, process_stage_id=process_stage_id, is_active=1).update(status = new_status, update_at = datetime.now())
            # transducerstatus_object = TransducerStatus.objects.all().order_by('stage_profile') 
            # data['html_transducerstatus_list'] = render_to_string('dashboard/transducerstatus_cud/partial_list.html', {
            #     'transducerstatusobject': transducerstatus_object
            # })
        else:
            print (request)
            print (form.errors)
            print (form.non_field_errors)
            data['form_is_valid'] = False

    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

def modulerequirementcreate_view(request):
    if request.method == 'POST':
        machine_rqmt = json.loads(request.POST['machine_rqmt'])

        # updated_request = request.POST.copy()
        # updated_request.update({'machine_rqmt': machine_rqmt[0]})

        # _mutable = request.POST._mutable

        # # set to mutable
        # request.POST._mutable = True

        # # сhange the values you want
        # request.POST['machine_rqmt'] = machine_rqmt[0]

        # # set mutable flag back
        # request._mutable = _mutable

        machinerequirement_object = MachineRequirement.objects.get(id=machine_rqmt[0])

        obj = ModuleRequirement.objects.create(title=request.POST['title'], machine_rqmt=machinerequirement_object)
        obj.save()
        # form = ModuleRequirementForm(request.POST)
        # form.fields['machine_rqmt'].choices = machine_rqmt[0]
    else:
        form = ModuleRequirementForm()
    return save_modulerequirement_form(request, form, 'dashboard/modulerequirement_cud/partial_create.html')