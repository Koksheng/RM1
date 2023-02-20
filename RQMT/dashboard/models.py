from django.db import models

# Create your models here.
class CommonInfo(models.Model):
    created_at                  = models.DateTimeField(auto_now_add = True, auto_now=False, verbose_name='Date Created')
    # updated_at                  = models.DateTimeField(auto_now = True, verbose_name='Date Changed')

    class Meta:
        abstract = True
        ordering = ['created_at']

class GeneralProcessStage(CommonInfo):
    id                      = models.AutoField(primary_key=True)
    process_stage_name      = models.CharField(max_length=50,verbose_name="Process Stage Name")
    software                = models.CharField(max_length=25,verbose_name="Software",blank=False)

    # when other place using "GeneralProcessStage.objects.all()" will return process_stage_name
    # def __str__(self):
    #     return self.process_stage_name

    class Meta:
        # verbose_name = "GeneralProcessStage"
        # verbose_name_plural = "GeneralProcessStages"
        db_table = 'general_process_stage'

class MachineRequirement(CommonInfo):
    id                      = models.CharField(primary_key=True, max_length=100, verbose_name='Machine Requirement Id')
    project_id              = models.CharField(max_length=100,verbose_name="Project Id")
    prs_id                  = models.IntegerField(verbose_name="PRS Id")
    title                   = models.CharField(max_length=255,verbose_name="Title")
    area                    = models.CharField(max_length=100,verbose_name="Area")
    description             = models.CharField(max_length=5000,verbose_name="Description")
    priority                = models.CharField(max_length=100,verbose_name="Priority")
    category                = models.CharField(max_length=100,verbose_name="Category")
    status                  = models.CharField(max_length=100,verbose_name="Status")
    type                    = models.CharField(max_length=100,verbose_name="Type")
    remarks                 = models.CharField(max_length=5000,verbose_name="Remarks")

    # when other place using "MachineRequirement.objects.all()" will return title
    def __str__(self):
        return self.title

    class Meta:
        db_table = 'RQMT_Machine_Requirement'

class ModuleRequirement(CommonInfo):
    id                      = models.AutoField(primary_key=True, max_length=100, verbose_name='Module Requirement Id')
    title                   = models.CharField(max_length=255,verbose_name="Title")
    machine_rqmt            = models.ForeignKey(MachineRequirement, on_delete=models.CASCADE, verbose_name='Machine Requirement')
    # availability            = models.CharField(max_length=100,verbose_name="Availability")

    class Meta:
        db_table = 'RQMT_Module_Requirement'