from dynamic_models.models import AbstractModelSchema, AbstractFieldSchema
from django.db import models
from datetime import date

class ModelSchema(AbstractModelSchema):
    pass

class FieldSchema(AbstractFieldSchema):
    pass


class ProjectManager(models.Manager):

    def create_project():
        project = Projects()
        project.save()

        transcription_table = create_transcription_table(project.title)
        return transcription_table

    def create_transcription_table(projectName):
        tableName = 'transcription_text_' + projectName
        transcription_table_model_schema = ModelSchema.objects.create(name=tableName)

        fileName_field_schema = FieldSchema.objects.create(name='fileName', data_type='character')
        transcription_text_field_schema = FieldSchema.objects.create(name='transcription_text', data_type='text')

        fileName = fileName_model_schema.add_field(
            fileName_field_schema,
            null=False,
            unique=False,
            max_length=128
        )

        transcription_text = transcription_text_model_schema.add_field(
            transcription_text_field_schema,
            null=False,
            unique=False,
        )

        return transcription_table_model_schema.as_model()


class Files(models.Model):
    file_name = models.CharField(max_length=256)
    transcription_text = models.TextField()
    uuid = models.CharField(max_length=256, null=True)
    question_name = models.CharField(max_length=256, null=True)


class Projects(models.Model):
    auth_user = models.CharField(max_length=128)
    api_key = models.CharField(max_length=256)
    asset_id = models.CharField(max_length=256)
    title = models.CharField(max_length=256)
    server_url = models.CharField(max_length=256)
    transcription_language = models.CharField(max_length=24)
    transcription_method = models.CharField(max_length=128)
    transcription_table = models.CharField(max_length=256)
    upload_date = models.DateField(default=date.today)

    objects = ProjectManager()
